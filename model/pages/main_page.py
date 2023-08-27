from selenium.webdriver.common.by import By

# --------------------------------- Ссылка каталога под полем поиска -------------------------------------------- #
HEADER_CATALOG_LINK = (By.CSS_SELECTOR, '[data-test-id=bottom-header-section-link]')
# ---------------------------------- Название товара в мини-карточке товара ------------------------------------- #
PRODUCT_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test-id=product-item-title] span')
# -------------------------------------- Картинка товара в мини-карточке товара --------------------------------- #
PRODUCT_IMAGE = (By.CSS_SELECTOR, '.m-image__image[src]')
# ------------------------- Кнопка "Каталог", отображаемая рядом со строкой поиска ------------------------------ #
CATALOG_MENU_BUTTON = (By.CSS_SELECTOR, '[data-test-id=catalog-btn]')
# -------------------- Заголовок категории в левой части страницы после нажатия кнопки "Каталог" ---------------- #
CATEGORY_TITLE = (By.XPATH, './/span[@data-test-id="left-catalog-item-title" '
                            'and not(contains(@class, "m-menu-item"))]')
# ----------------- Заголовок категории в левой части страницы по конкретному названию категории ---------------- #
CATEGORY_TITLE_WITH_PARAM = (By.XPATH, './/span[@data-test-id="left-catalog-item-title"][contains(text(),"{0}")]')
# --------------------- Название категории, которая сейчас открыта в главном окне ------------------------------- #
CATEGORY_TITLE_WHICH_OPEN_NOW = (By.XPATH, './/*[@data-test-id="category-title"]')
# ------------------------------------------- Кнопка сортировки по цене ----------------------------------------- #
SORT_BY_PRICE_BUTTON = (By.XPATH, './/button[@data-test-id="sort-price-btn"]')
# --------------------------------------------- Элемент товара -------------------------------------------------- #
PRODUCT = (By.XPATH, './/div[@data-test-id="product-item"]')
# --------------------------------------------- Наименование товара --------------------------------------------- #
PRODUCT_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]')
# ------------------------------------------------- Цена товара ------------------------------------------------- #
PRODUCT_PRICE = (By.XPATH, './/div[@data-test-id="product-item-price"]/span[1]')
# ---------------------------------------------- Старая цена товара --------------------------------------------- #
PRODUCT_OLD_PRICE = (By.XPATH, './/div[@data-test-id="product-item-price_old"]/span[1]')
# --------------------------------- Квант товара (минимальный шаг веса товара) ---------------------------------- #
PRODUCT_QUANT = (By.XPATH, './/div[@data-test-id="product-item-price"]/span[2]')
# ---------------------------------- Надпись у товара "Временно отсутствует" ------------------------------------ #
TEXT_PRODUCT_UNAVAILABLE = (By.XPATH, './/div[@class="product-card__info"]')
# ------------------------------------- Лоадер загрузки товаров (белый экран) ----------------------------------- #
PRODUCTS_LOADING_LOADER = (By.XPATH, './/div[@class="fade-enter-active fade-enter-to"]')
# -------------------------------- Активная кнопка сортировки по возрастанию цены ------------------------------- #
SORT_BY_ASCEND_PRICE_BUTTON = (By.XPATH, './/button[contains(@data-test-id,"sort-price-btn") and '
                                         'contains(@class,"decreasing")]')
# -------------------------------- Активная кнопка сортировки по убыванию цены ---------------------------------- #
SORT_BY_DESCEND_PRICE_BUTTON = (By.XPATH, './/button[contains(@data-test-id,"sort-price-btn") '
                                          'and contains(@class,"increasing")]')
# ---------------------------------------- Кнопка сортировки по алфавиту ---------------------------------------- #
SORT_BY_NAME_BUTTON = (By.XPATH, './/button[@data-test-id="sort-name-btn"]')
# ------------------------------------ Неактивная кнопка сортировки по алфавиту --------------------------------- #
SORT_BY_NAME_BUTTON_DISABLED = (By.XPATH, './/button[contains(@data-test-id,"sort-name-btn") '
                                          'and contains(@disable, "")]')
# -------------------------------------- Контент страницы каталога ---------------------------------------------- #
CATALOG_PAGE = (By.CSS_SELECTOR, '.js-paginator-scrolling-catalog-layout')
# ------------------------------------------- Логотип в хэдере--------------------------------------------------- #
HEADER_LOGO = (By.XPATH, './/*[@data-test-id="header-logo-link"]')
# --------------------------------- Контент главной страницы сайта ---------------------------------------------- #
HOME_PAGE = (By.CSS_SELECTOR, '.page-home')