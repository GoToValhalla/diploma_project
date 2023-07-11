from selenium.webdriver.common.by import By


class MainPage:
    """
    Локаторы главной страницы сайта и сквозных элементов.
    """
    # ------------------------------------------- Логотип в хэдере--------------------------------------------------- #
    HEADER_LOGO = (By.XPATH, './/*[@data-test-id="header-logo-link"]')

    # --------------------------------- Иконка входа в личный кабинет пользователя ---------------------------------- #
    LOGIN_ICON = (By.XPATH, './/*[@data-test-id="login-icon"]')
    # -------------------------------------- Кнопка "Корзина" в хедере сайта ---------------------------------------- #
    BASKET_BUTTON = (By.XPATH, './/div[@data-test-id="small-cart"]')
    # --------------------------------------- Время доставки в хедере сайта ----------------------------------------- #
    DELIVERY_TIME_TEXT = (By.CSS_SELECTOR, '.delivery-time')
    # ------------------------------------- Поп-ап "Укажите адрес доставки"------------------------------------------ #
    DELIVERY_ADDRESS_POPUP = (By.XPATH, './/div[@data-test-id="change-delivery-address-popup"]')
    # ------------------------- Поле ввода нового адреса в поп-апе "Укажите адрес доставки" ------------------------- #
    NEW_ADDRESS_FIELD_IN_POPUP = (By.XPATH, './/input[@data-test-id="delivery-address-input"]')
    # ---------------- Первый вариант в выпадающем списке ввода адреса в поп-апе "Укажите адрес доставки" ----------- #
    FIRST_OPTION_IN_DROPDOWN_LIST = (By.XPATH, './/section[@class="m-input-address__suggestions"]')
    # ----------------------------- Кнопка "Выбрать" в поп-апе "Укажите адрес доставки" ----------------------------- #
    SELECT_ADDRESS_BUTTON = (By.XPATH, './/button[@data-test-id="delivery-address-select-btn"]')
    # --------------------------------- Иконка корзины в хедере ----------------------------------------------------- #
    BASKET_ICON = (By.CSS_SELECTOR, '[data-test-id=small-cart] svg')
    # --------------------------------- Плашка адреса в хедере ------------------------------------------------------ #
    SELECT_ADDRESS_INNER = (By.CSS_SELECTOR, '.select-address__inner')
    # ------------------------------------- Поп-ап "Войти в личный кабинет" ----------------------------------------- #
    POPUP_LOGIN = (By.CSS_SELECTOR, '[data-test-id=login-popup]')
    # ---------- Поле ввода номера телефона в поп-апе "Войти в личный кабинет" и "Зарегистрироваться" --------------- #
    PHONE_NUMBER_FIELD = (By.XPATH, './/input[@data-test-id="input-phone"]')
    # ------------- Кнопка "Прислать SMS код" в поп-апе "Войти в личный кабинет" и "Зарегистрироваться" ------------- #
    SEND_SMS_CODE_BUTTON = (By.XPATH, './/*[@data-test-id="get-sms-code-btn"]')
    # ------------- Кнопка "Подтвердить" в поп-апе "Войти в личный кабинет" и "Зарегистрироваться"------------------- #
    CONFIRM_SMS_CODE_BUTTON = (By.XPATH, './/button[@data-test-id="confirm-sms-code-btn"]')
    # ---------------------------------- Текст на кнопке "Подтвердить" SMS код -------------------------------------- #
    TEXT_FROM_CONFIRM_SMS_CODE_BUTTON = (By.XPATH, './/button[@data-test-id="confirm-sms-code-btn"]//'
                                                   'span[@class="m-button__label"]')
    # --------------- Поле ввода sms кода в поп-апе "Войти в личный кабинет" и "Зарегистрироваться" ----------------- #
    SMS_CODE_FIELD = (By.XPATH, './/input[@data-test-id="input-sms-code"]')
    # ----------------------------- Поле ввода email кода в поп-апе "Напомнить пароль" ------------------------------ #
    EMAIL_CODE_FIELD = (By.XPATH, './/input[@data-test-id="input-code"]')
    # ------------------------ Кнопка "Войти по e-mail" в поп-апе "Войти в личный кабинет" -------------------------- #
    LOGIN_BY_EMAIL_BUTTON = (By.XPATH, './/button[@data-test-id="email-login-btn"]')
    # ------------------------ Кнопка "Войти по e-mail" в поп-апе "Войти в личный кабинет" -------------------------- #
    RECOVER_PASSWORD_LINK = (By.XPATH, './/div[@data-test-id="link-remind"]')
    # ----------------------- Кнопка "Восстановить пароль" в поп-апе "Напомнить пароль" ----------------------------- #
    RECOVER_PASSWORD_BUTTON = (By.XPATH, './/button[@data-test-id="remind-btn"]')
    # ----------------- Задизейбленная кнопка "Восстановить пароль" в поп-апе "Напомнить пароль" -------------------- #
    RECOVER_PASSWORD_BUTTON_DISABLED = (By.XPATH, './/button[@data-test-id="remind-btn" and contains(@class,'
                                                  '"is-disabled")]')
    # ----------------- Поле "E-mail" в поп-апе "Войти в личный кабинет" и "Зарегистрироваться" --------------------- #
    EMAIL_FIELD = (By.XPATH, './/input[@data-test-id="input-email"]')
    # ----------------------------- Поле "Пароль" в поп-апе "Войти в личный кабинет" -------------------------------- #
    PASSWORD_FIELD = (By.XPATH, './/input[@data-test-id="input-password"]')
    # ------------------------------ Кнопка "Войти" в поп-апе "Войти в личный кабинет" ------------------------------ #
    LOGIN_BUTTON = (By.XPATH, './/button[@data-test-id="login-btn"]')
    # ---------------------------------------- Кнопка "Зарегистрироваться" ------------------------------------------ #
    REGISTRATION_LINK_BUTTON = (By.XPATH, './/span[@data-test-id="link-register"]')
    # ---------------------------------------- Поп-ап "Зарегистрироваться" ------------------------------------------ #
    POPUP_REGISTRATION = (By.XPATH, './/div[@data-test-id="popup"]')
    # -------------------------------- Поле "Имя" в поп-апе "Зарегистрироваться" ------------------------------------ #
    USERNAME_FIELD = (By.XPATH, './/input[@data-test-id="input-name"]')
    # ------------------- Строка с таймером повторной отправки SMS в поп-апе "Зарегистрироваться"  ------------------ #
    TIMER_IN_REG_POPUP = (By.XPATH, './/div[@class="phone-verification-form__wait-new-sms"]')
    # ----------------------- Кнопка "Зарегистрироваться" в поп-апе "Зарегистрироваться"  --------------------------- #
    REGISTRATION_BUTTON_IN_POPUP = (By.XPATH, './/button[@data-test-id="registration-btn"]')
    # ---------------------------------------- Поп-ап "Напомнить пароль"  ------------------------------------------- #
    REMIND_PASSWORD_POPUP = (By.XPATH, './/div[@data-test-id="registration-popup"]')
    # ------------------------- Кнопка "Каталог", отображаемая рядом со строкой поиска ------------------------------ #
    CATALOG_MENU_BUTTON = (By.CSS_SELECTOR, '[data-test-id=catalog-btn]')
    # ------------------------- Левый блок с прокруткой после нажатия кнопки "Каталог" ------------------------------ #
    CATEGORY_CONTAINER = (By.XPATH, './/aside[@data-test-id="left-catalog"]')
    # ------------------------- Правый блок с прокруткой после нажатия кнопки "Каталог" ----------------------------- #
    SUBCATEGORY_CONTAINER = (By.XPATH, './/div[@data-test-id="subcatalog"]')
    # -------------------- Категория в левой части страницы после нажатия кнопки "Каталог" -------------------------- #
    CATEGORY_ITEM = (By.XPATH, './/li[@data-test-id="left-catalog-item"]')
    # -------------------- Заголовок категории в левой части страницы после нажатия кнопки "Каталог" ---------------- #
    CATEGORY_TITLE = (By.XPATH, './/span[@data-test-id="left-catalog-item-title" '
                                'and not(contains(@class, "m-menu-item"))]')
    # -------------------- Иконка категории в левой части страницы после нажатия кнопки "Каталог" ------------------- #
    CATEGORY_ICON = (By.XPATH, './/figure[@data-test-id="left-catalog-item-title" '
                               'and not(contains(@class, "m-menu-item"))]//img')
    # ----------------- Заголовок категории в левой части страницы по конкретному названию категории ---------------- #
    CATEGORY_TITLE_WITH_PARAM = (By.XPATH, './/span[@data-test-id="left-catalog-item-title"][contains(text(),"{0}")]')
    # ----------------- Кнопка подкатегории в правой части страницы по конкретному названию  ------------------------ #
    SUBCATEGORY_BUTTON_WITH_PARAM = (By.XPATH, './/*[@data-test-id="subcatalog-item"]//a[contains(text(),"{0}")]')
    # --------------------- Название категории, которая сейчас открыта в главном окне ------------------------------- #
    CATEGORY_TITLE_WHICH_OPEN_NOW = (By.XPATH, './/div[@data-test-id="category-title"]')
    # ---------------- Название категории, которая отображается после нажатия кнопки "Каталог" ---------------------- #
    LEFT_CATALOG_TITLE_WHICH_OPEN_NOW = (By.XPATH, './/div[@data-test-id="subcatalog-title"]')
    # --------------------- Кнопка подкатегории в правой части страницы после нажатия "Каталог" --------------------- #
    SUBCATEGORY_BUTTON = (By.XPATH, './/*[@data-test-id="subcatalog-item"]//a')
    # ------------------------------------------- Имя профиля в хедере ---------------------------------------------- #
    PROFILE_NAME_IN_HEADER = (By.CSS_SELECTOR, '[data-test-id=login-icon] .m-header-actions-item__label')
    # ----------------------------------- Окно малой корзины -------------------------------------------------------- #
    SMALL_BASKET = (By.XPATH, './/div[@class="m-header-mini-basket__inner"]')
    # ----------------------------------- Кнопка "В корзину" на главной --------------------------------------------- #
    HOME_BUY_BUTTON = (By.CSS_SELECTOR, '[data-test-id=products-section-product-card-buy-btn]')
    # ----------------------------------- Каунтер кнопки "Корзина" -------------------------------------------------- #
    COUNTER_BASKET = (By.CSS_SELECTOR, '.m-header-actions-item__count')
    # ----------------------------------- Поле поиска "Искать продукты" --------------------------------------------- #
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test-id=input-search]')
    # --------------------------------- Иконка "лупа" в поле поиска ------------------------------------------------- #
    SEARCH_ICON = (By.CSS_SELECTOR, '.m-input-search__icon')
    # --------------------------------- Предложения товаров в выпадающем списке поиска ------------------------------ #
    SUGGEST_SEARCH_ITEM = (
        By.XPATH, '//div[@data-test-id="suggest-search"]//div[2]//div[@data-test-id="suggest-search-item-title"]')
    # --------------------------------- Заголовок "Популярные запросы" в выпадающем списке поиска ------------------- #
    SEARCH_POPULAR_TITLE = (By.XPATH, '//span[@data-test-id="suggest-search-section-title"][contains(text(),'
                                      '"Популярные запросы")]')
    # --------------------------------- Заголовок "Товары" в выпадающем списке поиска ------------------------------- #
    SEARCH_PRODUCTS_TITLE = (By.XPATH, '//span[@data-test-id="suggest-search-section-title"][contains(text(),'
                                       '"Товары")]')
    # --------------------------------- Малая корзина, кнопка "+" в плашке товара ----------------------------------- #
    INCREASE_SMALL_BASKET_BUTTON = (By.CSS_SELECTOR, '.m-header-mini-basket__basket__content '
                                                     '[data-test-id=product-item-input-count-incr-btn]')
    # --------------------------------- Малая корзина, кнопка "-" в плашке товара ----------------------------------- #
    DECREASE_SMALL_BASKET_BUTTON = (By.CSS_SELECTOR, '.m-header-mini-basket__basket__content '
                                                     '[data-test-id=product-item-input-count-decr-btn]')
    # --------------------------------- Малая корзина, каунт в плашке товара ---------------------------------------- #
    SMALL_BASKET_COUNT = (By.CSS_SELECTOR, '.m-header-mini-basket__basket__content ['
                                           'data-test-id=product-item-input-count]')
    # --------------------------------- Малая корзина, инпут в плашке товара ---------------------------------------- #
    SMALL_BASKET_INPUT = (By.CSS_SELECTOR, '.m-header-mini-basket__basket__content .m-input-text.is-active input')
    # --------------------------------- Малая корзина, хинт о max кол-ве товара ------------------------------------- #
    MAX_QUANTITY_HINT = (By.CSS_SELECTOR, '.m-header-mini-basket__basket__content .m-tooltip__message.is-position--top')
    # --------------------------------- Ссылка каталога под полем поиска -------------------------------------------- #
    HEADER_CATALOG_LINK = (By.CSS_SELECTOR, '[data-test-id=bottom-header-section-link]')
    # --------------------------------- Контент главной страницы сайта ---------------------------------------------- #
    HOME_PAGE = (By.CSS_SELECTOR, '.page-home')
    # --------------------------------- Вывод ближайшей доставки по адресу ------------------------------------------ #
    DELIVERY_TIME_TOOLTIP = (By.CSS_SELECTOR, '.delivery-time-tooltip')
    # --------------------------------- Кнопка "Заказы" в хедере сайта ---------------------------------------------- #
    ORDERS_BUTTON = (By.XPATH, './/div[@data-test-id="orders-icon"]')
    # --------------------------------- Город в хедере сайта -------------------------------------------------------- #
    HEADER_CITY_TEXT = (By.CSS_SELECTOR, '.select-address__address h4')
    # --------------------------------- Улица в хедере сайта -------------------------------------------------------- #
    HEADER_STREET_TEXT = (By.CSS_SELECTOR, '.select-address__address p')
    # --------------------------------- Иконка "ВКонтакте" в футере ------------------------------------------------- #
    VK_ICON = (By.CSS_SELECTOR, 'img[alt="ВКонтакте"]')
    # --------------------------------- Иконка "Одноклассники" в футере --------------------------------------------- #
    OK_ICON = (By.CSS_SELECTOR, 'img[alt="Одноклассники"]')
    # --------------------------------- Иконка "Твиттер" в футере --------------------------------------------------- #
    TWITTER_ICON = (By.CSS_SELECTOR, 'img[alt="Твиттер"]')
    # --------------------------------- Валидационное сообщение под полем "Код из SMS" ------------------------------ #
    INPUT_SMS_VALIDATION_TEXT = (By.CSS_SELECTOR, '[data-test-id=input-sms-code] span')
    # --------------------------------- Валидационное сообщение под полем "E-mail" ---------------------------------- #
    INPUT_EMAIL_VALIDATION_TEXT = (By.CSS_SELECTOR, '[data-test-id=input-email] span')
    # --------------------------------- Валидационное сообщение под полем "Пароль" ---------------------------------- #
    INPUT_PASSWORD_VALIDATION_TEXT = (By.CSS_SELECTOR, '[data-test-id=input-password] span')
    # --------------------------------- Поп-ап "Адрес доставки"------------------------------------------------------ #
    DELIVERY_ADDRESS_SELECT_POPUP = (By.CSS_SELECTOR, '[data-test-id=delivery-address-popup]')
    # --------------------------------- Выпадающий список адресов доставки в поп-апе "Адрес доставки" --------------- #
    DROPDOWN_DELIVERY_ADDRESS = (By.CSS_SELECTOR, '[data-test-id=dropdown-delivery-address]')
    # --------------------------------- Кнопка "Добавить новый адрес" в поп-апе "Адрес доставки" -------------------- #
    ADD_DELIVERY_ADDRESS_BUTTON = (By.CSS_SELECTOR, '[data-test-id=add-delivery-address-btn]')
    # --------------------------------- Кнопка очищения поля "крестик" в поп-апе ------------------------------------ #
    ADDRESS_INPUT_CLEAR_BUTTON = (By.CSS_SELECTOR, '[data-test-id=delivery-address-input-clear-field-btn]')
    # ----------------- Плашка с сохраненным адресом в выпадающем списке по названию -------------------------------- #
    DELIVERY_ADDRESS_ITEM_PARAM = (By.XPATH, './/*[@data-test-id="delivery-address-item"]//div[contains(text(),"{0}")]')
    # ----------------- Кнопка "Сохранить" в поп-апе "Адрес доставки" ----------------------------------------------- #
    USER_ADDRESS_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.m-modal-user-address-manager__submit')
    # ---------------------------------- Кнопка "Изменить" в поп-апе менеджера адресов ------------------------------ #
    CHANGE_ADDRESS_POPUP_BUTTON = (By.XPATH, './/*[@data-test-id="delivery-address-change-btn"]')
    # -------------------------- Кнопка закрытия поп-апа "Пока нет доставки по вашему адресу" ----------------------- #
    IMPOSSIBLE_DELIVERY_POPUP_CLOSE_BUTTON = (
        By.XPATH,
        './/*[@data-test-id="impossible-delivery-address-popup"]/parent::*'
        '//*[@data-test-id="close-popup-btn"]',
    )
    # ----------------- Секция с ссылками правовой информации в футере ---------------------------------------------- #
    LEGAL_INFO_SECTION = (By.CSS_SELECTOR, '[data-test-id=legal-info-section]')
    # ----------------- Заголовок ссылки "Правовая информация" в футере --------------------------------------------- #
    INFORMATION_LEGAL_LINK_TITLE = (By.CSS_SELECTOR, '[href="/information-legal/"] span')
    # ----------------- Заголовок ссылки "Пользовательское соглашение" в футере ------------------------------------- #
    USER_SOGLAS_LINK_TITLE = (By.CSS_SELECTOR, '[href="/user_soglas"] span')
    # ----------------- Заголовок ссылки "Политика обработки персональных данных" в футере -------------------------- #
    PERSONAL_DATA_POLITICS_LINK_TITLE = (By.CSS_SELECTOR, '[href="/personal_data_politics"] span')
    # ----------------- Заголовок ссылки "Политика конфиденциальности" в футере ------------------------------------- #
    POLICY_PRIVACY_LINK_TITLE = (By.CSS_SELECTOR, '[href="/policy_privacy"] span')
    # ----------------- Ссылка "Правовая информация" в футере ------------------------------------------------------- #
    INFORMATION_LEGAL_LINK = (By.CSS_SELECTOR, '[href="/information-legal/"]')
    # ---------------------------------- Контент "Правовая информация" ---------------------------------------------- #
    INFORMATION_LEGAL_CONTENT = (By.CSS_SELECTOR, '[pathmatch="information-legal/"]')
    # ---------------------------------- Поп-ап регистрации данных пользователя ------------------------------------- #
    REGISTRATION_POPUP = (By.CSS_SELECTOR, '[data-test-id=registration-popup]')
    # ---------------------------------- Кнопка закрыть (крестик) в поп-апе ----------------------------------------- #
    CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, '[data-test-id=close-popup-btn]')
    # ------------------------- Валидационное сообщение под полем "Номер телефона" в поп-апе ------------------------ #
    INPUT_PHONE_VALIDATION_TEXT = (By.CSS_SELECTOR, '[data-test-id=input-phone] span')
    # ------------------------------------------- Логотип в футере -------------------------------------------------- #
    FOOTER_LOGO = (By.CSS_SELECTOR, '[data-test-id=footer-logo-link]')
    # ------------------------------------ Телефон поддержки в хедере ----------------------------------------------- #
    HEADER_SUPPORT_PHONE = (By.CSS_SELECTOR, '.m-navigation__phone')
    # ------------------------------------ Телефон поддержки в футере ----------------------------------------------- #
    FOOTER_SUPPORT_PHONE = (By.CSS_SELECTOR, '[data-test-id=footer-support-phone]')
    # ------------------------------ Подсказка под телефоном поддержки в футере ------------------------------------- #
    FOOTER_SUPPORT_PHONE_HELPER = (By.CSS_SELECTOR, '.m-tel__helper')
    # ------------------------------------ Ссылка "Контакты" в футере ----------------------------------------------- #
    CONTACTS_LINK = (By.XPATH, './/span[contains(text(),"Контакты")]')
    # ------------------------------------ Ссылка "Информация о компании" в футере ---------------------------------- #
    COMPANY_INFO_LINK = (By.CSS_SELECTOR, '[href="/company-Information"]')
    # ------------------------------------ Контент страницы "Информация о компании" --------------------------------- #
    COMPANY_INFO_CONTENT = (By.CSS_SELECTOR, '[pathmatch="company-Information"]')
    # ------------------------------------ Ссылка "Оплата" в футере ------------------------------------------------- #
    PAYMENTS_LINK = (By.XPATH, './/span[contains(text(),"Оплата")]')
    # ------------------------------------ Ссылка "Вопросы и ответы" в футере --------------------------------------- #
    FAQ_LINK = (By.XPATH, './/span[contains(text(),"Вопросы и ответы")]')

    # ------------------------------------- Заголовок страницы "Поддержка" ------------------------------------------ #
    FAQ_TITLE = (By.XPATH, './/h3[@class="profile-personal-support__title text--h3-profile"]')
    # ------------------------------- Блок с телефоном на странице "Поддержка" -------------------------------------- #
    PHONE_NUMBER_SECTION = (By.XPATH, './/div[@class="support-contacts__container"]')
    # --------------------------- Блок часто задаваемых вопросов на странице "Поддержка" ---------------------------- #
    FAQ_SECTION = (By.XPATH, './/div[@class="profile-personal-support__faq faq"]')
    # --------------------------- Параграф "Оплата и возврат денег" на странице "Поддержка" ------------------------- #
    PAYMENT_AND_REFUND_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Оплата и возврат денег")]')
    # ---------------------- Открытый параграф "Оплата и возврат денег" на странице "Поддержка" --------------------- #
    PAYMENT_AND_REFUND_PARAGRAPH_OPENED = (By.XPATH, './/div[@class="faq__paragraph paragraph is-open"]/'
                                                     'div[contains(text(),"Оплата и возврат денег")]')
    # ------------------- Блок вопросов параграфа "Оплата и возврат денег" на странице "Поддержка" ------------------ #
    QUESTIONS_OF_PAYMENT_AND_REFUND_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Оплата и возврат денег")]/'
                                                           'following-sibling::div')
    # ------------------------------- Параграф "Изменения в заказе" на странице "Поддержка" ------------------------- #
    ORDER_CHANGES_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Изменения в заказе")]')
    # ------------------------ Открытый параграф "Изменения в заказе" на странице "Поддержка" ----------------------- #
    ORDER_CHANGES_PARAGRAPH_OPENED = (By.XPATH, './/div[@class="faq__paragraph paragraph is-open"]/'
                                                'div[contains(text(),"Изменения в заказе")]')
    # ----------------------- Блок вопросов параграфа "Изменения в заказе" на странице "Поддержка" ------------------ #
    QUESTIONS_OF_ORDER_CHANGES_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Изменения в заказе")]/'
                                                      'following-sibling::div')
    # -------------------------------- Параграф "Возврат товара" на странице "Поддержка" ---------------------------- #
    PURCHASE_RETURNS_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Возврат товара")]')
    # --------------------------- Открытый параграф "Возврат товара" на странице "Поддержка" ------------------------ #
    PURCHASE_RETURNS_PARAGRAPH_OPENED = (By.XPATH, './/div[@class="faq__paragraph paragraph is-open"]/'
                                                   'div[contains(text(),"Возврат товара")]')
    # ----------------------- Блок вопросов параграфа "Возврат товара" на странице "Поддержка" ---------------------- #
    QUESTIONS_OF_PURCHASE_RETURNS_PARAGRAPH = (By.XPATH, './/div[contains(text(),"Возврат товара")]/'
                                                         'following-sibling::div')

    # ------------------------------------ Ссылка "Правила возврата" в футере --------------------------------------- #
    RETURN_RULES_LINK = (By.XPATH, './/span[contains(text(),"Правила возврата")]')
    # --------------------------------- Лоадер в каунтере товара в малой корзине ------------------------------------ #
    SMALL_BASKET_COUNT_LOADER = (By.XPATH, './/div[@class="m-spinner-round"]/span[@class="m-spinner-round__spinner"]')
    # --------------------------- Параграф "Оплата и возврат денег" на странице "Поддержка" ------------------------- #

    # ------------------------------------ Большой баннер на главной странице --------------------------------------- #
    BIG_BANNER = (By.XPATH, './/section[contains(@class,"swiper") and contains(@class,"page")]')
    # ---------------------------------- Ссылка в большом банере главной страницы ----------------------------------- #
    BIG_BANNER_LINK = (By.XPATH, './/div[contains(@class, "active") and contains(@class, "slide")][1]/a')
    # -------------------------------------- Картинка большого баннера до активации --------------------------------- #
    BIG_BANNER_PICTURE_BEFORE_ACTIVE = (By.XPATH, './/div[@class="swiper-slide"][1]//img[contains(@src,"")]')
    # ---------------------------------------- Активная картинка большого баннера ----------------------------------- #
    ACTIVE_BIG_BANNER_PICTURE = (By.XPATH, './/div[contains(@class,"swiper-slide-active")]//img[contains(@src,"")]')
    # ----------------------------------- Отобразить следующий баннер (кнопка вправо) ------------------------------- #
    NEXT_BANNER_RIGHT_BUTTON = (By.XPATH, './/button[contains(@class,"wiper-controls-next") and not (@disabled)]')
