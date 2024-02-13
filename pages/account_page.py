from .base_page import BasePage
from .locators import AccountLocators


class AccountPage(BasePage):
    def is_success_message_present(self) -> bool:
        return self.is_element_present(*AccountLocators.SUCCESS_MESSAGE)

    def get_user_data(self) -> str:
        return self.browser.find_element(*AccountLocators.USER_DATA).text
