from selenium.webdriver.common.by import By
from test_data.links import JUNO_JACKET_PRODUCT_PAGE_LINK


class BasePageLocators:
    CART_PRODUCTS_NUMBER = (By.CLASS_NAME, "counter-number")
    # EMPTY_CART = (By.CSS_SELECTOR, "a.showcart > span.counter.empty")
    # NOT_EMPTY_CART = (By.CSS_SELECTOR, "a.showcart > .counter")
    CART_COUNTER = (By.CSS_SELECTOR, "a.showcart > span.counter")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")


class CreateAccountPageLocators:
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button.submit")
    FIRST_NAME_ERROR = (By.ID, "firstname-error")
    LAST_NAME_ERROR = (By.ID, "lastname-error")
    EMAIL_ERROR = (By.ID, "email_address-error")
    PASSWORD_ERROR = (By.ID, "password-error")
    CONFIRM_PASSWORD_ERROR = (By.ID, "password-confirmation-error")
    SAME_USER_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-error']")


class AccountPageLocators:
    USER_DATA = (By.CSS_SELECTOR, ".box-information .box-content p")
    SIGN_OUT_LINK = (By.CSS_SELECTOR, ".authorization-link > a")
    CUSTOMER_MENU_TOGGLE = (By.CSS_SELECTOR, ".page-header [data-action='customer-menu-toggle']")


class ProductPageLocators:
    # sizes
    XS_SIZE = (By.ID, "option-label-size-143-item-166")
    S_SIZE = (By.ID, "option-label-size-143-item-167")
    M_SIZE = (By.ID, "option-label-size-143-item-168")
    L_SIZE = (By.ID, "option-label-size-143-item-169")
    XL_SIZE = (By.ID, "option-label-size-143-item-170")

    # colors
    BLACK_COLOR = (By.ID, "option-label-color-93-item-49")
    ORANGE_COLOR = (By.ID, "option-label-color-93-item-56")
    YELLOW_COLOR = (By.ID, "option-label-color-93-item-60")

    ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")


class ProductListPageLocators:
    # sizes
    XS_SIZE = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-size-143-item-166")
    S_SIZE = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-size-143-item-167")
    M_SIZE = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-size-143-item-168")
    L_SIZE = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-size-143-item-169")
    XL_SIZE = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-size-143-item-170")

    # colors
    BLUE_COLOR = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-color-93-item-50")
    GREEN_COLOR = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-color-93-item-53")
    PURPLE_COLOR = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div #option-label-color-93-item-57")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, f"a[href='{JUNO_JACKET_PRODUCT_PAGE_LINK}'] + div button.tocart")


class CartPageLocators:
    ITEM_OPTIONS = (By.CSS_SELECTOR, ".item-options > dd")
