from selenium.webdriver.common.by import By


class CreateAccountLocators:
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


class AccountLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")
    USER_DATA = (By.CSS_SELECTOR, ".box-information .box-content p")
    SIGN_OUT_LINK = (By.CSS_SELECTOR, ".authorization-link > a")
    CUSTOMER_MENU_TOGGLE = (By.CSS_SELECTOR, ".page-header [data-action='customer-menu-toggle']")

