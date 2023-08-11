import allure
from selene.support.shared import browser
from model.pages.base_page import Base_page


def test_add_address_delivery():
    base_page = Base_Page()
    with allure.step('Кликаем на форму указания адреса'):
        browser.open("https://dostavka.magnit.ru/")
        base_page.add_address_delivery
