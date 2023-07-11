import allure
from selene.support.shared import browser
from selene import have, by



def test_open_main_page(setap_browser):
    browser = setap_browser


#TODO  Дописать проверки
with allure.step('Открываем стартовую страницу'):
    browser.open('https://dostavka.magnit.ru/')
    browser.element('[data-test-id="header-logo-link"]').should()