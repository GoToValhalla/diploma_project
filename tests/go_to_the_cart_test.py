from pytest import mark
import allure
from model.pages.base_page import BasePage


@mark.smoke
@mark.regress
def test_go_to_the_cart():
    base_page = BasePage()

    with allure.step('Открываем сайт доставки'):
        base_page.open()

    with allure.step('Кликаем на корзину'):
        base_page.go_to_cart()

    with allure.step('Возвращаемся на главную'):
        base_page.go_to_main_page_button()

    with allure.step('Проверяем, что вернулись на главную станицу'):
        base_page.logo()

# TODO открывается попап с адресом
