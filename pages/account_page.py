from .base_page import BasePage
from .locators import AccountPageLocators
from test_data.user import User


class AccountPage(BasePage):
    def __get_user_data(self) -> dict:
        user_info = self.browser.find_element(*AccountPageLocators.USER_DATA).text
        user_info_list = user_info.split("\n")
        user_info_dict = {
            "name": user_info_list[0].strip(),
            "email": user_info_list[1].strip()
        }
        return user_info_dict

    def new_user_data_should_be_consistent(self, user: User):
        user_info = self.__get_user_data()

        assert (user_info["name"] == user.full_name and user_info["email"] == user.email), \
            (f"The account information isn't correct.\n"
             f"Received: user name '{user_info["name"]}', user email '{user_info["email"]}'.\n"
             f"Expected: user name '{user.full_name}', user email '{user.email}'\n.")

    def sign_out(self):
        self.browser.find_element(*AccountPageLocators.CUSTOMER_MENU_TOGGLE).click()
        self.browser.find_element(*AccountPageLocators.SIGN_OUT_LINK).click()
