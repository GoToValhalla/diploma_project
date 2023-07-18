from selenium.webdriver.common.by import By


class Catalog_page:

    # --------------------------------------------- Элемент товара -------------------------------------------------- #
    PRODUCT = (By.XPATH, './/div[@data-test-id="product-item"]')
    # --------------------------------------------- Наименование товара --------------------------------------------- #
    PRODUCT_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]')
    # ------------------------------------ Товар в каталоге по определённому имени ---------------------------------- #
    PRODUCT_BY_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]//span[contains(text(),"{0}")]')

    # ------------------------------------------------- Цена товара ------------------------------------------------- #
    PRODUCT_PRICE = (By.XPATH, './/div[@data-test-id="product-item-price"]/span[1]')
    # -------------------------------------- Цена товара (обязательно со скидкой) ----------------------------------- #
    PRODUCT_DISCOUNT_PRICE = (By.XPATH, (
        './/div[@data-test-id="product-item-price" and contains(concat(" ", @class, " "), "is-discounted")]/span[1]'
    ))
    # -------------------------------------- Цена товара со скидкой у заданного товара ------------------------------ #
    PRODUCT_DISCOUNT_PRICE_BY_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]/span[contains(text(),'
                                                '"{0}")]/../../following-sibling::div/div/div[@data-test-id='
                                                '"product-item-price"]')
    # ---------------------------------------------- Старая цена товара --------------------------------------------- #
    PRODUCT_OLD_PRICE = (By.XPATH, './/div[@data-test-id="product-item-price_old"]/span[1]')
    # ---------------------------------- Старая цена у заданного товара (цена до скидки) ---------------------------- #
    PRODUCT_PRICE_BY_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]/span[contains(text(),"{0}")]/../../'
                                       'following-sibling::div/div/div[@data-test-id="product-item-price"]/'
                                       'following-sibling::div')

    # ---------------------------------------- Лейбл "Скидка" у заданного товара ------------------------------------ #
    PRODUCT_DISCOUNT_LABEL_BY_NAME = (By.XPATH, './/div[@data-test-id="product-item-title"]/span[contains(text(),'
                                                '"{0}")]/../../preceding-sibling::div/div[@class="m-badge badge"]')
    # ---------------------------------- Название товара в мини-карточке товара ------------------------------------- #
    PRODUCT_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test-id=product-item-title] span')



    # ------------------------------------------------- СОРТИРОВКА -------------------------------------------------- #
    # ------------------------------------------- Кнопка сортировки по цене ----------------------------------------- #
    SORT_BY_PRICE_BUTTON = (By.XPATH, './/button[@data-test-id="sort-price-btn"]')
    # -------------------------------- Активная кнопка сортировки по возрастанию цены ------------------------------- #
    SORT_BY_ASCEND_PRICE_BUTTON = (By.XPATH, './/button[contains(@data-test-id,"sort-price-btn") and '
                                             'contains(@class,"decreasing")]')
    # -------------------------------- Активная кнопка сортировки по убыванию цены ---------------------------------- #
    SORT_BY_DESCEND_PRICE_BUTTON = (By.XPATH, './/button[contains(@data-test-id,"sort-price-btn") '
                                              'and contains(@class,"increasing")]')
    # ---------------------------------------- Список доступных сортировок ------------------------------------------ #
    CATALOG_SORT_LIST = (By.CSS_SELECTOR, '.catalog-sort__list')
    # ------------------------------------ Кнопка сортировки "По популярности" -------------------------------------- #
    SORT_POPULAR_BUTTON = (By.CSS_SELECTOR, '[data-test-id="sort-popular-btn"]')

    # ------------------------------------- Лоадер загрузки товаров (белый экран) ----------------------------------- #
    PRODUCTS_LOADING_LOADER = (By.XPATH, './/div[@class="fade-enter-active fade-enter-to"]')
    # -------------------------- Лоадер загрузки товаров (появляется после применения фильтров) -------------------- #
    PRODUCTS_LOADERS_AFTER_FILTER = (By.XPATH, './/div[@class="card-loader product__container product_border"][1]')

    # ------------------------------------------------- ФИЛЬТРАЦИЯ -------------------------------------------------- #
    # -------------------------------------- Переключатель "Товары со скидкой" -------------------------------------- #
    DISCOUNT_ONLY_TOGGLE = (By.CSS_SELECTOR, '*[data-test-id="filter-toggler-btn"]')
    # ---------------------------- Переключатель "Товары со скидкой" (выключенное положение) ------------------------ #
    DISCOUNT_ONLY_TOGGLE_OFF = (By.XPATH, './/div[@data-test-id="filter-toggler-btn"]/'
                                          'div[@class="m-switch__btn__switch m-switch__btn__switch_left"]')
    # ------------------------------- Задизейбленный переключатель "Товары со скидкой" ------------------------------ #
    DISCOUNT_ONLY_TOGGLE_DISABLE = (By.XPATH, './/div[@data-test-id="filter-toggler" and contains(@class,'
                                              '"m-switch--disabled")]')

    # --------------------------------------------- Блок фильтра цены ----------------------------------------------- #
    PRICE_FILTER_SECTION = (By.XPATH, './/section[@data-test-id="filter-price"]')
    # --------------------------------------- Фильтр по цене (мин. значение) ---------------------------------------- #
    MIN_PRICE_FILTER = (By.XPATH, './/input[@data-test-id="filter-price-input-from"]')
    # ----------------------------------- Задизейбленый фильтр цены (мин значение)  --------------------------------- #
    MIN_PRICE_FILTER_DISABLE = (By.XPATH, './/input[@data-test-id="filter-price-input-from" and contains(@disabled, '
                                          '"disabled")]')
    # --------------------------------------- Фильтр по цене (макс. значение) --------------------------------------- #
    MAX_PRICE_FILTER = (By.XPATH, './/input[@data-test-id="filter-price-input-to"]')
    # ----------------------------------- Задизейбленый фильтр цены (макс значение)  -------------------------------- #
    MAX_PRICE_FILTER_DISABLE = (By.XPATH, './/input[@data-test-id="filter-price-input-to" and contains(@disabled, '
                                          '"disabled")]')
    # ------------------------------------------ Кнопка "Сбросить фильтры" ------------------------------------------ #
    FILTER_CLEAR_BUTTON = (By.XPATH, './/button[@data-test-id="filter-clear-btn"]')
    # ------------------------------------- Неактивная кнопка "Сбросить фильтры" ------------------------------------ #
    DISABLED_FILTER_CLEAR_BUTTON = (By.XPATH, './/button[@data-test-id="filter-clear-btn" and contains(@class, '
                                              '"is-disabled")]')
    # --------------------------------- Чекбокс фильтра внутри определённого фильтра--------------------------------- #
    CHECKBOX_IN_SPECIFIC_FILTER = (By.XPATH, '(//div[@data-test-id="filter-variant"])[{0}]'
                                             '//div[@class="checkbox-list__wrapper"]//section/ul/li/label/span[1]')

    # -------------------------------------------- Блок любого фильтра ---------------------------------------------- #
    FILTER_SECTION = (By.XPATH, './/div[@data-test-id="filter-variant"]')
