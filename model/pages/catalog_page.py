from selene.support.shared import browser


class Catalog_page:

    def catalog_baton(self):
        browser.element('[data-test-id="catalog-btn"]')
        return self
