import allure
from model.pages.base_page import Base_page


def test_add_address_delivery():
    base_page = Base_page()
    with allure.step('Кликаем на форму указания адреса'):
        base_page.open()
        base_page.add_address_delivery
