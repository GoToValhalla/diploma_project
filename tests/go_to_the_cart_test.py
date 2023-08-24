# from pytest import mark
# import allure
# from model.pages.base_page import BasePage
#
#
# @mark.smoke
# @mark.regress
# def test_go_to_the_cart():
#     base_page = BasePage()
#
#     with allure.step('Открываем сайт доставки'):
#         base_page.open()
#
#     with allure.step('Кликаем на корзину'):
#         base_page.go_to_cart()
#
#     with allure.step('Возвращаемся на главную'):
#         base_page.go_to_main_page_button()
#
#     with allure.step('Проверяем, что вернулись на главную станицу'):
#         base_page.logo()
#
# # TODO открывается попап с адресом


from random import choice

from allure import title

from pages.main_page import (assert_equally_category_name,
                             assert_equally_product_name, assert_open_catalog_page,
                             assert_open_home_page, assert_product_list_sort_by_name,
                             assert_product_list_sorted_by_price,
                             assert_product_name_mini_card_is_present,
                             assert_selected_category_is_open,
                             assert_sort_ascend_price_button_is_active,
                             assert_sort_by_name_button_disabled,
                             assert_sort_descend_price_button_is_active,
                             click_catalog_menu_button, click_header_catalog_link,
                             click_header_logo,
                             click_on_category_in_left_part_of_screen,
                             click_product_image_from_mini_card,
                             click_sort_by_name_button, click_sort_by_price_button,
                             get_categories, open_main_page)


@title('Клик по картинке товара вызывает переход в карточку товара')
def test_open_product_card_from_catalog():
    open_main_page()
    category_title = click_header_catalog_link()
    assert_equally_category_name(category_title)

    assert_product_name_mini_card_is_present()
    first_product_name = click_product_image_from_mini_card()
    assert_equally_product_name(first_product_name)


@title('Сортировка товара по цене')
def test_sort_by_price():
    open_main_page()
    click_catalog_menu_button()

    category = choice(get_categories())
    click_on_category_in_left_part_of_screen(category=category)
    assert_selected_category_is_open(expected_category_name=category)

    # ШАГ №1
    click_sort_by_price_button()
    assert_product_list_sorted_by_price(price_ascending=True)
    assert_sort_ascend_price_button_is_active()

    # ШАГ №2
    click_sort_by_price_button()
    assert_product_list_sorted_by_price(price_ascending=False)
    assert_sort_descend_price_button_is_active()


@title('Сортировка товара по алфавиту')
def test_sort_by_alphabet():
    open_main_page()
    click_catalog_menu_button()
    category = choice(get_categories())
    click_on_category_in_left_part_of_screen(category=category)
    assert_selected_category_is_open(expected_category_name=category)

    click_sort_by_name_button()
    assert_product_list_sort_by_name()
    assert_sort_by_name_button_disabled()


@title('Переход на главную страницу при клике по логотипу в хедере')
def test_logo_header():
    open_main_page()

    click_header_catalog_link()
    assert_open_catalog_page()

    click_header_logo()
    assert_open_home_page()

# pip install allure-pytest
