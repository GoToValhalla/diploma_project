import dataclasses
from selene.support.shared import browser


class Base_page:

    def open(self):
        browser.open('https://dostavka.magnit.ru/')
    def cart(self):
        browser.element('[data-test-id="small-cart"]')
