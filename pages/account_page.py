from .base_page import BasePage
from .locators import AccountLocators


class AccountPage(BasePage):
    def is_success_message_present(self) -> bool:
        return self.is_element_present(*AccountLocators.SUCCESS_MESSAGE)

    def get_user_data(self) -> str:
        return self.browser.find_element(*AccountLocators.USER_DATA).text

    def sign_out(self):
        self.browser.find_element(*AccountLocators.CUSTOMER_MENU_TOGGLE).click()
        self.browser.find_element(*AccountLocators.SIGN_OUT_LINK).click()
