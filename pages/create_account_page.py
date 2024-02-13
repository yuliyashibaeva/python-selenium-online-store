from .base_page import BasePage
from .locators import CreateAccountLocators


class CreateAccountPage(BasePage):
    CREATE_ACCOUNT_LINK = "https://magento.softwaretestingboard.com/customer/account/create/"

    def create_new_account(self, user_data: dict):
        self.browser.find_element(*CreateAccountLocators.FIRST_NAME).send_keys(user_data["first_name"])
        self.browser.find_element(*CreateAccountLocators.LAST_NAME).send_keys(user_data["last_name"])
        self.browser.find_element(*CreateAccountLocators.EMAIL).send_keys(user_data["user_email"])
        self.browser.find_element(*CreateAccountLocators.PASSWORD).send_keys(user_data["user_password"])
        self.browser.find_element(*CreateAccountLocators.PASSWORD_CONFIRMATION).send_keys(user_data["user_password"])
        self.browser.find_element(*CreateAccountLocators.CREATE_ACCOUNT_BUTTON).click()

