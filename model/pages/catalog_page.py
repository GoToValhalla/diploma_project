from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class CatalogPage:

    def catalog_baton(self):
        s('[data-test-id="catalog-btn"]').click()
        return self
