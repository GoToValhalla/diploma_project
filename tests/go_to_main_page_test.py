from selene.support.shared import browser
from selene import have, be
import allure
from selene.support.shared.jquery_style import s

def test_open_main_page():
    with allure.step('Открываем стартовую страницу'):
        browser.open('https://dostavka.magnit.ru/')
        s('[data-test-id="header-logo-link"]').should(have.exact_text('Магнит Доставка'))

