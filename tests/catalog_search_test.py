import time

import allure
from model.pages.base_page import BasePage
from model.pages.catalog_page import CatalogPage


def test_catalog_search():
    base_page = BasePage()
    catalog_page = CatalogPage()

    with allure.step('Открываем сайт доставки'):
        base_page.open()
    time.sleep(5)
    with allure.step('Кликаем на кнопку каталог'):
        catalog_page.catalog_baton()


pass
