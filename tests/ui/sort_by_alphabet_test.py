from random import choice
from allure import title

from model.step.catalog_page import *
from model.step.main_page import *


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
