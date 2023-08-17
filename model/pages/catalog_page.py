from selene.support.shared import browser


class CatalogPage:

    def catalog_baton(self):
        browser.element('[data-test-id="catalog-btn"]').click()
        return self
