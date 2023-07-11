import allure
from selene.support.shared import browser
from selene import have, by


class Base_page:
    @allure.title('Переходим на стартовую страницу')
    def test_open_main_page(setap_browser):
        browser = setap_browser

    with allure.step('Открываем стартовую страницу'):
        browser.open('https://dostavka.magnit.ru/')
        browser.element('[data-test-id="header-logo-link"]').should(have.exact_text('Магнит Доставка'))