
from re import sub
from time import sleep

from allure import step

from model.pages.main_page import *
from model.step.base import *


# --------------------------------------------------- catalog_page -------------------------------------------------- #

@step('Появление и ожидание исчезновения лоадера загрузки товаров')
def loader_wait():
    """
    Появление и ожидание исчезновения лоадера загрузки товаров
    """
    is_element_present(*PRODUCTS_LOADING_LOADER, timeout=0.5)
    is_not_element_present(*PRODUCTS_LOADING_LOADER)


@step('Получить список товаров со страницы')
def get_product_list(is_available_products=True, have_old_price_products=None):
    """
    Получить список товаров со страницы.
    :param is_available_products: Получить список только доступных к покупке товаров.
    :param have_old_price_products: Получить список товаров, доступных для покупки, и у которых есть старая цена.
    """
    loader_wait()

    products_el = driver.find_elements(*PRODUCT)
    product_list_all = []
    available_products_list = []
    products_with_old_price = []

    for element in products_el:
        name = element.find_element(*PRODUCT_NAME).text
        price = sub(r'[^.,\d]', '', element.find_element(*PRODUCT_PRICE).text)
        price = price.replace(',', '.')

        try:
            old_price = sub(r'[^.,\d]', '', element.find_element(*PRODUCT_OLD_PRICE).text)
            old_price = old_price.replace(',', '.')
        except Exception:
            old_price = 0

        # проверка, весовой ли товар
        try:
            product_quant_element = element.find_element(*PRODUCT_QUANT).text
            if '₽/' in product_quant_element:
                is_weight = True
            else:
                is_weight = False
        except Exception:
            is_weight = 0

        # проверка доступен ли товар для покупки
        try:
            element.find_element(*TEXT_PRODUCT_UNAVAILABLE)
            is_available = False
        except Exception:
            is_available = True

        if is_available:
            available_products_list.append({'name': name, 'price': float(price), 'old_price': float(old_price),
                                            'is_weight': is_weight,
                                            'is_available_products': is_available_products})

        product_list_all.append({'name': name, 'price': float(price), 'old_price': float(old_price),
                                 'is_weight': is_weight, 'is_available_products': is_available_products})
        if old_price != 0 and is_available:
            products_with_old_price.append({'name': name, 'price': float(price), 'old_price': float(old_price),
                                            'is_weight': is_weight,
                                            'is_available_products': is_available_products})

    if is_available_products:
        return available_products_list
    elif have_old_price_products:
        return products_with_old_price
    else:
        return product_list_all


@step('Клик по кнопке сортировки по цене')
def click_sort_by_price_button():
    """
    Клик по кнопке сортировки по цене.
    """
    driver.find_element(*SORT_BY_PRICE_BUTTON).click()


@step('Клик по кнопке сортировки по цене')
def click_sort_by_price_button():
    """
    Клик по кнопке сортировки по цене.
    """
    is_element_present(*SORT_BY_PRICE_BUTTON, timeout=5)
    find_element_clickable(*SORT_BY_PRICE_BUTTON).click()


@step('Клик по кнопке сортировки по алфавиту')
def click_sort_by_name_button():
    """
    Клик по кнопке сортировки по алфавиту.
    """
    find_element_clickable(*SORT_BY_NAME_BUTTON).click()


@step('Проверить, что список товаров отсортирован по алфавиту')
def assert_product_list_sort_by_name():
    """
    Проверить, что список товаров отсортирован по алфавиту.
    """
    # получение списка товаров с сайта
    product_list_from_catalog = get_product_list(is_available_products=False)

    # создание списка со строчными именами товаров
    products_list_from_catalog_in_lower_case = [x['name'].lower() for x in product_list_from_catalog]

    # сортировка списка имён товаров
    new_sort_list = products_list_from_catalog_in_lower_case
    new_sort_list.sort()

    # сравнение сортированного списка и списка с сайта, формирование списка различий
    products_with_wrong_sort = []
    for i in range(0, len(product_list_from_catalog)):
        if products_list_from_catalog_in_lower_case[i] != new_sort_list[i]:
            products_with_wrong_sort.append(product_list_from_catalog[i]['name'])

    assert products_with_wrong_sort == [], f'Следующие товары не отсортированы по алфавиту: ' \
                                           f'{products_with_wrong_sort}'


@step('Проверить, что кнопка сортировки по алфавиту неактивна')
def assert_sort_by_name_button_disabled():
    """
    Проверить, что кнопка сортировки по алфавиту неактивна.
    """
    sort_by_name_button_is_disabled = is_element_present(*SORT_BY_NAME_BUTTON_DISABLED)
    assert sort_by_name_button_is_disabled, 'Кнопка сортировки по алфавиту доступна для нажатия'


@step('Проверить открытие страницы каталога')
def assert_open_catalog_page():
    """
    Проверить, что открыта страница каталога
    """
    assert is_element_present(*CATALOG_PAGE), 'Страница каталога не открыта!'


@step('Проверить, что список товаров отсортирован по возрастанию или убыванию цены')
def assert_product_list_sorted_by_price(price_ascending=True):
    """
    Проверить, что список товаров отсортирован по возрастанию или убыванию цены.
    :param price_ascending: True - если проверяется сортировка по возрастанию цены, False - если по убыванию.
    """
    # получение списка товаров
    product_list_from_catalog_after_sort = get_product_list(is_available_products=False)

    # получение нового списка для последующего применения сортировки
    new_product_list = product_list_from_catalog_after_sort

    # сортировка по возрастанию или убыванию
    if price_ascending:
        new_sorted_product_list = sorted(new_product_list, key=lambda k: k['price'])
    else:
        new_sorted_product_list = sorted(new_product_list, key=lambda k: k['price'], reverse=True)

    # сравнение нового отсортированного списка и списка с сайта, формирование списка различий
    products_with_wrong_sort = []
    for i in range(0, len(product_list_from_catalog_after_sort)):
        if product_list_from_catalog_after_sort[i] != new_sorted_product_list[i]:
            products_with_wrong_sort.append(product_list_from_catalog_after_sort[i]['name'])

    assert products_with_wrong_sort == [], f'Следующие товары не отсортированы по цене: {products_with_wrong_sort}'


@step('Проверить, что кнопка сортировки по возрастанию цены активна')
def assert_sort_ascend_price_button_is_active():
    """
    Проверить, что кнопка сортировки по возрастанию цены активна.
    """
    sort_by_ascend_price_button_is_active = is_element_present(*SORT_BY_ASCEND_PRICE_BUTTON)
    assert sort_by_ascend_price_button_is_active, 'Кнопка сортировки по возрастанию цены не активна'


@step('Проверить, что кнопка сортировки по убыванию цены активна')
def assert_sort_descend_price_button_is_active():
    """
    Проверить, что кнопка сортировки по убыванию цены активна.
    """
    sort_by_descend_price_button_is_active = is_element_present(*SORT_BY_DESCEND_PRICE_BUTTON)
    assert sort_by_descend_price_button_is_active, 'Кнопка сортировки по убыванию цены не активна'