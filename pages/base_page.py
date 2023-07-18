from selenium.webdriver.common.by import By



class Base_page:
    # ------------------------------------- Поп-ап "Укажите адрес доставки"------------------------------------------ #
    DELIVERY_ADDRESS_POPUP = (By.XPATH, './/div[@data-test-id="change-delivery-address-popup"]')
    # ------------------------- Поле ввода нового адреса в поп-апе "Укажите адрес доставки" ------------------------- #
    NEW_ADDRESS_FIELD_IN_POPUP = (By.XPATH, './/input[@data-test-id="delivery-address-input"]')
    # ---------------- Первый вариант в выпадающем списке ввода адреса в поп-апе "Укажите адрес доставки" ----------- #
    FIRST_OPTION_IN_DROPDOWN_LIST = (By.XPATH, './/section[@class="m-input-address__suggestions"]')
    # ----------------------------- Кнопка "Выбрать" в поп-апе "Укажите адрес доставки" ----------------------------- #
    SELECT_ADDRESS_BUTTON = (By.XPATH, './/button[@data-test-id="delivery-address-select-btn"]')
    # ------------------------- Кнопка "Каталог", отображаемая рядом со строкой поиска ------------------------------ #
    CATALOG_MENU_BUTTON = (By.CSS_SELECTOR, '[data-test-id=catalog-btn]')
    # ----------------------------------- Поле поиска "Искать продукты" --------------------------------------------- #
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test-id=input-search]')
    # --------------------------------- Иконка "лупа" в поле поиска ------------------------------------------------- #
    SEARCH_ICON = (By.CSS_SELECTOR, '.m-input-search__icon')
    # --------------------------------- Кнопка очищения поля "крестик" в поп-апе ------------------------------------ #
    ADDRESS_INPUT_CLEAR_BUTTON = (By.CSS_SELECTOR, '[data-test-id=delivery-address-input-clear-field-btn]')
    # ------------------------- Кнопка "Каталог", отображаемая рядом со строкой поиска ------------------------------ #
    CATALOG_MENU_BUTTON = (By.CSS_SELECTOR, '[data-test-id=catalog-btn]')
