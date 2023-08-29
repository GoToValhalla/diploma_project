import time

import allure
from model.step.main_page import *



# TODO не находит меню ввода адресса доставки
def test_select_adress():
    open_main_page()
    click_select_address_inner()
    a = 0
