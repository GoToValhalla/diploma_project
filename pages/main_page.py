from re import sub
from time import sleep

from allure import step
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from main_page_locators import (CATALOG_MENU_BUTTON, CATALOG_PAGE,
                                CATEGORY_TITLE, CATEGORY_TITLE_WHICH_OPEN_NOW,
                                CATEGORY_TITLE_WITH_PARAM, HEADER_CATALOG_LINK,
                                HEADER_LOGO, HOME_PAGE, PRODUCT, PRODUCT_IMAGE,
                                PRODUCT_ITEM_TITLE, PRODUCT_NAME,
                                PRODUCT_OLD_PRICE, PRODUCT_PRICE,
                                PRODUCT_QUANT, PRODUCTS_LOADING_LOADER,
                                SORT_BY_ASCEND_PRICE_BUTTON,
                                SORT_BY_DESCEND_PRICE_BUTTON,
                                SORT_BY_NAME_BUTTON,
                                SORT_BY_NAME_BUTTON_DISABLED,
                                SORT_BY_PRICE_BUTTON, TEXT_PRODUCT_UNAVAILABLE)

# options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
# driver = webdriver.Chrome(options=options)


# ------------------------------------------------------ base ------------------------------------------------------- #

def is_element_present(strategy, locator, timeout=3.0) -> bool:
    """
    Проверка и ожидание появления элемента на странице.
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((strategy, locator)),
        )
    except TimeoutException:
        return False
    return True


def is_not_element_present(strategy, locator, timeout=3.0) -> bool:
    """
    Проверка и ожидание исчезновения элемента на странице.
    """
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.presence_of_element_located((strategy, locator)),
        )
    except TimeoutException:
        return False
    return True


def find_element_clickable(strategy, locator, timeout=3.0):
    """
    Поиск кликабельного элемента на странице.
    :return: найденный веб-элемент.
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((strategy, locator)),
        message=f'Элемент с локатором: {(strategy, locator)} не доступен более {timeout} секунд',
    )
    scroll_to_element(element)
    return element


def scroll_to_element(element):
    """
    Прокрутка страницы до элемента.
    """

    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element)
    y_window = driver.execute_script('return window.pageYOffset')
    window_size = driver.execute_script('return document.documentElement.clientHeight')

    timer = 0
    while timer < 3:
        if (element.location['y'] >= y_window) and (
                element.location['y'] + element.size['height'] < y_window + window_size):
            break
        else:
            sleep(0.5)
            timer += 1


# ---------------------------------------------------- main_page ---------------------------------------------------- #

@step('Открыть главную страницу')
def open_main_page():
    driver.get('https://dostavka.magnit.ru/')


@step('Кликнуть по первой найденной ссылке каталога под полем поиска')
def click_header_catalog_link():
    """
    Клик по первой найденной ссылке каталога под полем поиска.
    :return: название категории каталога
    """

    element = driver.find_element(*HEADER_CATALOG_LINK)
    element_text = element.text
    element.click()
    return element_text


@step('Кликнуть по фото первого найденного товара')
def click_product_image_from_mini_card() -> str:
    """
    Клик по фото первого товара в мини-карточке товара.
    :return: название товара в мини-карточке товара
    """
    element = find_element_clickable(*PRODUCT_ITEM_TITLE)
    element_text = element.text
    find_element_clickable(*PRODUCT_IMAGE).click()
    return element_text


@step('Кликнуть по кнопке "Каталог"')
def click_catalog_menu_button():
    """
    Кликнуть по кнопке "Каталог".
    """
    driver.find_element(*CATALOG_MENU_BUTTON).click()


@step('Получить список категорий с главной страницы сайта')
def get_categories():
    """
    Получение списка категорий, появляющийся после нажатия кнопки "Каталог".
    :return: список наименований категорий.
    """

    categories_list = []
    categories = driver.find_elements(*CATEGORY_TITLE)
    for i in categories:
        categories_list.append(i.text)
    return categories_list


@step('Кликнуть по заданной категории в левой части страницы')
def click_on_category_in_left_part_of_screen(category: str):
    """
    Кликнуть по заданной категории в левой части страницы.
    :param category: Категория, по которой необходимо кликнуть.
    """
    strategy, locator = CATEGORY_TITLE_WITH_PARAM
    driver.find_element(strategy, locator.format(category)).click()


@step('Кликнуть по логотипу в хедере')
def click_header_logo():
    """
    Клик по логотипу в хедере.
    """
    find_element_clickable(*HEADER_LOGO).click()


@step('Проверка отображения названия товара в мини-карточке')
def assert_product_name_mini_card_is_present():
    """
    Проверить, что отображается название товара в мини-карточке
    """
    product_name = is_element_present(*PRODUCT_ITEM_TITLE)
    assert product_name, 'Название товара в мини-карточке отсутствует'


@step('Проверить название товара в карточке товара')
def assert_equally_product_name(expected_name: str):
    """
    Проверить, что название товара в мини-карточке совпадает с названием товара в карточке.
    :param expected_name: Ожидаемое название товара
    """
    product_name = driver.find_element(*PRODUCT_ITEM_TITLE).text
    assert (product_name == expected_name), \
        f'Название товара не совпадает, ожидается: {expected_name}, фактически: {product_name}'


@step('Проверить, что выбранная категория открыта')
def assert_selected_category_is_open(expected_category_name: str):
    """
    Проверить, что выбранная категория открыта.
    :param expected_category_name: Имя категории, которую необходимо проверить, что она открыта.
    """
    is_element_present(*CATEGORY_TITLE_WHICH_OPEN_NOW, timeout=5.0)
    text_in_category_name = driver.find_element(*CATEGORY_TITLE_WHICH_OPEN_NOW).text
    assert text_in_category_name == expected_category_name, f'Название открытой категории не совпадает с ' \
                                                            f'ожидаемым: "{expected_category_name}"'


@step('Проверить открытие главной')
def assert_open_home_page():
    """
    Проверить, что открыта главная страница
    """
    assert is_element_present(*HOME_PAGE), 'Главная страница не открыта'


@step('Проверить название категории каталога')
def assert_equally_category_name(expected_name: str):
    """
    Проверить, что название категории каталога соответствует названию в ссылке.
    :param expected_name: Ожидаемое название категории каталога
    """
    category_name = driver.find_element(*HEADER_CATALOG_LINK).text
    assert (category_name == expected_name), \
        f'Название категории каталога ошибочно, ожидается: {expected_name}, фактически: {category_name}'


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
