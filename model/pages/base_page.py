import dataclasses
from selene.support.shared import browser


class Base_page:

    def open(self):
        browser.open('https://dostavka.magnit.ru/')
        return self
    def cart(self):
        browser.element('[data-test-id="small-cart"]')
        return self
    def add_address_delivery(self):
        browser.element('[class="select-address__address"]').click()
        return self
    def logo(self):
        browser.element('[data-test-id="header-logo-link"]')
        return self

    def go_to_main_page_button(self):
        browser.element('[data-test-id="to-main-btn"]')
        return self
