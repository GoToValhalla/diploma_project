import allure
from model.pages.base_page import BasePage


def test_add_address_delivery():
    base_page = BasePage()
    with allure.step('Кликаем на форму указания адреса'):
        base_page.open()
        base_page.add_address_delivery
