import allure
from selene.support.shared import browser


def test_catalog_search():

    with allure.step('Открываем сайт доставки'):
        browser.open('https://dostavka.magnit.ru/')