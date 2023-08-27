from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver


# ------------------------------------------------------ base ------------------------------------------------------- #

def is_element_present(strategy, locator, timeout=3.0) -> bool:
    """
    Проверка и ожидание появления элемента на странице.
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((strategy, locator)),
        )
    except TimeoutException:
        return False
    return True


def is_not_element_present(strategy, locator, timeout=3.0) -> bool:
    """
    Проверка и ожидание исчезновения элемента на странице.
    """
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.presence_of_element_located((strategy, locator)),
        )
    except TimeoutException:
        return False
    return True


def find_element_clickable(strategy, locator, timeout=3.0):
    """
    Поиск кликабельного элемента на странице.
    :return: найденный веб-элемент.
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((strategy, locator)),
        message=f'Элемент с локатором: {(strategy, locator)} не доступен более {timeout} секунд',
    )
    scroll_to_element(element)
    return element


def scroll_to_element(element):
    """
    Прокрутка страницы до элемента.
    """

    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element)
    y_window = driver.execute_script('return window.pageYOffset')
    window_size = driver.execute_script('return document.documentElement.clientHeight')

    timer = 0
    while timer < 3:
        if (element.location['y'] >= y_window) and (
                element.location['y'] + element.size['height'] < y_window + window_size):
            break
        else:
            sleep(0.5)
            timer += 1