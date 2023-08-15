import allure
from model.pages.base_page import Base_page


def test_go_to_the_cart():
    base_page = Base_page

    with allure.step('Переходим в корзину'):
        base_page.open()
        base_page.go_to_cart()
        base_page.logo().should()

    with allure.step('Возвращение на главную страницу'):
        base_page.go_to_main_page_button().click()
        base_page.logo().should()

# TODO ошибка в тесте.
