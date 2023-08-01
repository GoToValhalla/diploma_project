import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome import options


def get_option():
    return webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path='/Users/user/chromedriver-mac-x64/chromedriver',
                          options=options,
                          desired_capabilities=get_option().to_capabilities())



@pytest.fixture()
def test1():
    return 555


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    browser.config.window_width = 1400
    browser.config.window_height = 1200
    browser.config.base_url = 'https://demoqa.com'
