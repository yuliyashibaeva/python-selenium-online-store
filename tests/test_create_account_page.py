from pages.create_account_page import CreateAccountPage
from pages.account_page import AccountPage
import pytest


class TestCreateNewUser:
    def test_new_user_account_should_be_created(self, browser, user_data):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CreateAccountPage.CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user_data)
        create_account_page.click_create_account_button()
        account_page = AccountPage(browser)
        assert account_page.is_success_message_present(), \
            "A new user wasn't created: there is no success message on the account page"

    def test_new_user_account_data_should_be_consistent(self, browser, user_data):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CreateAccountPage.CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user_data)
        create_account_page.click_create_account_button()
        account_page = AccountPage(browser)
        user_contact_info = account_page.get_user_data().split("\n")

        assert (user_contact_info[0].strip() == user_data['full_name']
                and user_contact_info[1].strip() == user_data['user_email']), \
            (f"The account information isn't correct.\n"
             f"Received: user name '{user_contact_info[0].strip()}', user email '{user_contact_info[1].strip()}'.\n"
             f"Expected: user name '{user_data['full_name']}', user email '{user_data['user_email']}'.")


class TestCreateUserValidations:
    @pytest.mark.parametrize("skip_field_name", CreateAccountPage.FIELD_NAMES)
    def test_creation_new_account_without_required_field_should_cause_invalid_marker_and_error_message(self, browser, user_data, skip_field_name):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CreateAccountPage.CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user_data)
        create_account_page.clear_field(skip_field_name)
        create_account_page.click_create_account_button()

        assert (create_account_page.is_field_marked_as_invalid(skip_field_name)
                and create_account_page.is_error_message_under_field_present(skip_field_name)), \
            (f"The validation didn't worked. Either the field '{skip_field_name}' "
             f"doesn't marked as invalid or there is no error message.")
