from selene.support.shared.jquery_style import s
from selene.support.shared import browser


class BasePage:

    def open(self):
        browser.open('https://dostavka.magnit.ru/')
        return self

    def go_to_cart(self):
        s('[data-test-id="small-cart"]').click()
        return self

    def add_address_delivery(self):
        s('[class="select-address__address"]').click()
        return self

    def logo(self):
        s('[data-test-id="header-logo-link"]').click()
        return self

    def go_to_main_page_button(self):
        s('[data-test-id="to-main-btn"]').click()
        return self
