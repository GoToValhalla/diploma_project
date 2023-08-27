from allure import title

from model.step.main_page import *


@title('Клик по картинке товара вызывает переход в карточку товара')
def test_open_product_card_from_catalog():
    open_main_page()
    category_title = click_header_catalog_link()
    assert_equally_category_name(category_title)

    assert_product_name_mini_card_is_present()
    first_product_name = click_product_image_from_mini_card()
    assert_equally_product_name(first_product_name)