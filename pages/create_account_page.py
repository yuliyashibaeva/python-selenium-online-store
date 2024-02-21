from .base_page import BasePage
from .locators import CreateAccountPageLocators
from test_data.user import User


class CreateAccountPage(BasePage):

    def click_create_account_button(self):
        self.browser.find_element(*CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def clear_field(self, field_name):
        self.browser.find_element(*self.__get_field_locator(field_name)).clear()

    def enter_user_account_data(self, user: User):
        self.browser.find_element(*self.__get_field_locator("first_name")).send_keys(user.first_name)
        self.browser.find_element(*self.__get_field_locator("last_name")).send_keys(user.last_name)
        self.browser.find_element(*self.__get_field_locator("email")).send_keys(user.email)
        self.browser.find_element(*self.__get_field_locator("password")).send_keys(user.password)
        self.browser.find_element(*self.__get_field_locator("confirm_password")).send_keys(user.password)

    def error_message_should_be_present(self, field_name: str):
        assert self.is_element_present(*self.__get_error_message_field_locator(field_name)), \
            f"There is no error message under the field '{field_name}'."

    def field_should_be_marked(self, field_name: str):
        assert (self.browser.find_element(*self.__get_field_locator(field_name)).get_attribute("aria-invalid")
                == "true"), f"The field {field_name} isn't marked as invalid."

    @staticmethod
    def __get_error_message_field_locator(field_name: str) -> tuple:
        return BasePage.get_locator(CreateAccountPageLocators, field_name + "_ERROR")

    @staticmethod
    def __get_field_locator(field_name: str) -> tuple:
        return BasePage.get_locator(CreateAccountPageLocators, field_name)

    def same_user_error_message_should_be_present(self):
        assert self.is_element_present(*CreateAccountPageLocators.SAME_USER_ERROR_MESSAGE), \
            "There is no error message that a user with this email has been registered."
