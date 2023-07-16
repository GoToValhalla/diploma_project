import time

import allure
from selene.support.shared import browser


def test_add_address_delivery():
    with allure.step('Кликаем на форму указания адреса'):
        browser.open('https://dostavka.magnit.ru/')
    browser.element('[class="select-address__tooltip"]').click()
    with allure.step('Ставим фокус в форму ввода адреса доставки'):
        browser.element('[data-test-id="delivery-address-input"]').click()

    # time.sleep(20)

    with allure.step('Вводим адрес доставки'):
        browser.element('[class="m-input-text__input"]').send_keys('москва тверская 10с1')
        browser.element('[class="m-input-address__suggestions__item"]').click()
    with allure.step('Подтверждаем введенный адрес'):
        browser.element('[data-test-id="delivery-address-select-btn"]').click()


time.sleep(20)
