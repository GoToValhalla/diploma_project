import allure
from selene.support.shared import browser
from model.pages.catalog_page import *


def test_go_to_the_cart(Base_page=None):
    base_page = Base_page
    # catalog_page = Catalog_page
    with allure.step('Переходим в корзину'):
        base_page.open()
        base_page.cart().click()
        base_page.logo().should()

    with allure.step('Возвращение на главную страницу'):
        base_page.go_to_main_page_button().click()
        base_page.logo().should()

#TODO ошибка в тесте.