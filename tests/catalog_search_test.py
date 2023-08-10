import allure
from selene.support.shared import browser
from model.pages import *
from model.pages import base_page
from model.pages.base_page import Base_page
from model.pages.catalog_page import Catalog_page


def test_catalog_search():

    with allure.step('Открываем сайт доставки'):
        base_page = Base_page()
        catalog_page = Catalog_page()
        base_page.open()

    with allure.step('Кликаем на кнопку каталог'):
        catalog_page.catalog_baton().click()





pass