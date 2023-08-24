from random import choice

from allure import title

from pages.main_page import (assert_product_list_sorted_by_price,
                             assert_selected_category_is_open,
                             assert_sort_ascend_price_button_is_active,
                             assert_sort_descend_price_button_is_active,
                             click_catalog_menu_button,
                             click_on_category_in_left_part_of_screen,
                             click_sort_by_price_button,
                             get_categories, open_main_page)


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
