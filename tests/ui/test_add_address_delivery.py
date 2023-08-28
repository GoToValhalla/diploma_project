import time

import allure
from model.step.main_page import *


def test_add_address_delivery():
    with allure.step('Кликаем на форму указания адреса'):
        open_main_page()
        time.sleep(5)
#TODO не находит меню ввода адресса доставки
        click_delivery_address()
        input_delivery_address()
