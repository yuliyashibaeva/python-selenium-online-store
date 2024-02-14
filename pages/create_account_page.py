from .base_page import BasePage
from .locators import CreateAccountLocators


class CreateAccountPage(BasePage):
    CREATE_ACCOUNT_LINK = "https://magento.softwaretestingboard.com/customer/account/create/"
    FIELD_NAMES = ["first_name", "last_name", "email", "password", "confirm_password"]

    def enter_user_account_data(self, user_data: dict):
        for field_name in CreateAccountPage.FIELD_NAMES:
            self.enter_in_field(field_name, self.__choose_value_from_user_data_dict(user_data, field_name))

    def enter_in_field(self, field_name: str, data_to_enter: str):
        self.browser.find_element(*self.__get_field_locator(field_name)).send_keys(data_to_enter)

    def click_create_account_button(self):
        self.browser.find_element(*CreateAccountLocators.CREATE_ACCOUNT_BUTTON).click()

    def clear_field(self, field_name):
        self.browser.find_element(*self.__get_field_locator(field_name)).clear()

    def is_field_marked_as_invalid(self, field_name: str) -> bool:
        return self.browser.find_element(*self.__get_field_locator(field_name)).get_attribute("aria-invalid") == "true"

    def is_error_message_under_field_present(self, field_name: str) -> bool:
        return self.is_element_present(*self.__get_error_message_locator(field_name))

    @staticmethod
    def __get_field_locator(field_name: str) -> tuple:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return CreateAccountLocators.FIRST_NAME
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return CreateAccountLocators.LAST_NAME
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return CreateAccountLocators.EMAIL
        elif field_name == CreateAccountPage.FIELD_NAMES[3]:
            return CreateAccountLocators.PASSWORD
        elif field_name == CreateAccountPage.FIELD_NAMES[4]:
            return CreateAccountLocators.CONFIRM_PASSWORD
        else:
            return None

    @staticmethod
    def __get_error_message_locator(field_name: str) -> tuple:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return CreateAccountLocators.FIRST_NAME_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return CreateAccountLocators.LAST_NAME_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return CreateAccountLocators.EMAIL_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[3]:
            return CreateAccountLocators.PASSWORD_ERROR
        elif field_name == CreateAccountPage.FIELD_NAMES[4]:
            return CreateAccountLocators.CONFIRM_PASSWORD_ERROR
        else:
            return None

    @staticmethod
    def __choose_value_from_user_data_dict(user_data: dict, field_name: str) -> str:
        if field_name == CreateAccountPage.FIELD_NAMES[0]:
            return user_data["first_name"]
        elif field_name == CreateAccountPage.FIELD_NAMES[1]:
            return user_data["last_name"]
        elif field_name == CreateAccountPage.FIELD_NAMES[2]:
            return user_data["user_email"]
        elif field_name == CreateAccountPage.FIELD_NAMES[3] or field_name == CreateAccountPage.FIELD_NAMES[4]:
            return user_data["user_password"]
        else:
            return None