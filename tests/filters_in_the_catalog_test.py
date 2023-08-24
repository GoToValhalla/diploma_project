import time

import allure
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from selene.support.shared.jquery_style import s


def test_catalog_search():
    base_page = BasePage()
    catalog_page = CatalogPage()

    with allure.step('Открываем сайт доставки'):
        base_page.open()
    time.sleep(5)
    with allure.step('Кликаем на кнопку каталог'):
        s('[data-test-id="catalog-btn"]').click()
        s('[data-test-id="left-catalog"]')

    with allure.step('Выбираем категорию'):
        s('[href="/express/catalog/moloko_syr_yaytsa"]').click()

    with allure.step('Возвращаемся на главную'):
        base_page.logo()

#TODO дописать проверки