import allure
from selene.support.shared import browser


@allure.title('Переходим на стартовую страницу')
def test_catalog_search():
    with allure.step('Открываем стартовую страницу'):
        browser.open('https://dostavka.magnit.ru/')
