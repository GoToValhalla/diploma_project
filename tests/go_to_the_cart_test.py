import allure
from selene.support.shared import browser
from model.pages.catalog_page import *


def test_go_to_the_cart(Base_page=None):
    base_page = Base_page
    # catalog_page = Catalog_page
    with allure.step('Переходим в корзину'):
        base_page.open()
        browser.element('[data-test-id="small-cart"]').click()
        browser.element('[data-test-id="header-logo-link"]').should()

    with allure.step('Возвращение на главную страницу'):
        browser.element('[data-test-id="to-main-btn"]').click()
        browser.element('[data-test-id="header-logo-link"]').should()

#TODO ошибка в тесте.