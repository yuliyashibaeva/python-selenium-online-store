from .base_page import BasePage
from .locators import CreateAccountPageLocators
from test_data.user import User


class CreateAccountPage(BasePage):
    FIELD_NAMES = ["first_name", "last_name", "email", "password", "confirm_password"]

    def click_create_account_button(self):
        self.browser.find_element(*CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def clear_field(self, field_name):
        self.browser.find_element(*self.__get_field_locator(field_name)).clear()

    def enter_in_field(self, field_name: str, data_to_enter: str):
        self.browser.find_element(*self.__get_field_locator(field_name)).send_keys(data_to_enter)

    def enter_user_account_data(self, user: User):
        for field_name in CreateAccountPage.FIELD_NAMES:
            self.enter_in_field(field_name, self.__choose_value_from_user_data_dict(user, field_name))

    def error_message_and_invalid_marker_should_be_present(self, field_name):
        assert self.is_error_message_under_field_present(field_name) and self.is_field_marked_as_invalid(field_name), \
            (f"The validation didn't worked. "
             f"Either the field '{field_name}' doesn't marked as invalid or there is no error message.")

    def is_error_message_under_field_present(self, field_name: str) -> bool:
        return self.is_element_present(*self.__get_error_message_locator(field_name))

    def is_field_marked_as_invalid(self, field_name: str) -> bool:
        return self.browser.find_element(*self.__get_field_locator(field_name)).get_attribute("aria-invalid") == "true"

    def same_user_error_message_should_be_present(self):
        assert self.is_element_present(*CreateAccountPageLocators.SAME_USER_ERROR_MESSAGE), \
            "There is no error message that a user with this email has been registered."

    @staticmethod
    def __get_error_message_locator(field_name: str) -> tuple:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return CreateAccountPageLocators.FIRST_NAME_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return CreateAccountPageLocators.LAST_NAME_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return CreateAccountPageLocators.EMAIL_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[3]:
            return CreateAccountPageLocators.PASSWORD_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[4]:
            return CreateAccountPageLocators.CONFIRM_PASSWORD_ERROR
        else:
            return None

    @staticmethod
    def __get_field_locator(field_name: str) -> tuple:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return CreateAccountPageLocators.FIRST_NAME
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return CreateAccountPageLocators.LAST_NAME
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return CreateAccountPageLocators.EMAIL
        elif field_name == CreateAccountPage.FIELD_NAMES[3]:
            return CreateAccountPageLocators.PASSWORD
        elif field_name == CreateAccountPage.FIELD_NAMES[4]:
            return CreateAccountPageLocators.CONFIRM_PASSWORD
        else:
            return None

    @staticmethod
    def __choose_value_from_user_data_dict(user: User, field_name: str) -> str:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return user.first_name
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return user.last_name
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return user.email
        elif field_name == CreateAccountPage.FIELD_NAMES[3] or field_name == CreateAccountPage.FIELD_NAMES[4]:
            return user.password
        else:
            return None