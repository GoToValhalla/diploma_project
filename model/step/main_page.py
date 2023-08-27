from allure import step

from model.pages.main_page import *
from model.step.base import *


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