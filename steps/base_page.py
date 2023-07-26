import allure
from pages import base_page
from selene.support.shared import browser


class main_page:

    @allure.title('Переходим на стартовую страницу')
    def open_main_page(self):
        with allure.step('Открываем стартовую страницу'):
            browser.open('https://dostavka.magnit.ru/')
