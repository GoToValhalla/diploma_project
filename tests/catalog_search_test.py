import allure
import by
from selene.support.shared import browser


def test_catalog_search():

    with allure.step('Открываем сайт доставки'):
        browser.open('https://dostavka.magnit.ru/')

    with allure.step('Кликаем на кнопку каталог'):
        browser.element('[data-test-id="catalog-btn"]').click()


    with allure.step(''):
        $(by.LINK_TEXT('Цена — что надо')).click()




pass