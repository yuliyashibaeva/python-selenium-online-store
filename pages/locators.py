from selenium.webdriver.common.by import By


class CreateAccountLocators:
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRMATION = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button.submit")


class AccountLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")
    USER_DATA = (By.CSS_SELECTOR, ".box-information .box-content p")
