import allure
from selene.support.shared import browser
import pages.base_page


def test_search_by_category():

    with allure.step('Переходим на главную  станицу'):
        # browser.open('https://dostavka.magnit.ru/')
        pages.base_page.Base_page.test_open_main_page()