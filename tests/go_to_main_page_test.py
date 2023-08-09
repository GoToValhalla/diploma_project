from selene.support.shared import browser
from selene import have, be
import allure

def test_open_main_page():
    with allure.step('Открываем стартовую страницу'):
        browser.open('https://dostavka.magnit.ru/')
        browser.element('[data-test-id="header-logo-link"]').should(have.exact_text('Магнит Доставка'))

