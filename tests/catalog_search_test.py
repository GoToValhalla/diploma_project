import allure
from selene.support.shared import browser
from model.pages import *
from model.pages import base_page


def test_catalog_search(Base_page=None):

    with allure.step('Открываем сайт доставки'):
        base_page = Base_page
        base_page.open()

    with allure.step('Кликаем на кнопку каталог'):
        browser.element('[data-test-id="catalog-btn"]').click()





pass