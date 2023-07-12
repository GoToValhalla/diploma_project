import allure
from selene.support.shared import browser


def test_add_address_delivery():
    with allure.step('Кликаем на форму указания адреса'):
        browser.open('https://dostavka.magnit.ru/')
    browser.element('[class="select-address__tooltip"]').click()



