import allure
from selene.support.shared import browser


def test_go_to_the_cart():


    with allure.step('Переходим в корзину'):
        browser.open('https://dostavka.magnit.ru/')
        browser.element('[data-test-id="small-cart"]').click()

    with allure.step('Возвращение на главную страницу'):
        browser.element('[data-test-id="to-main-btn"]').click()
