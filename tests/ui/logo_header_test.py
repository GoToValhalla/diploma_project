from allure import title

from model.step.catalog_page import assert_open_catalog_page
from model.step.main_page import *


@title('Переход на главную страницу при клике по логотипу в хедере')
def test_logo_header():
    open_main_page()

    click_header_catalog_link()
    assert_open_catalog_page()

    click_header_logo()
    assert_open_home_page()
