from pages.create_account_page import CreateAccountPage
from pages.account_page import AccountPage
from test_data.links import CREATE_ACCOUNT_LINK
import pytest


@pytest.mark.smoke
class TestCreateNewUser:
    def test_new_user_account_should_be_created(self, browser, user):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user)
        create_account_page.click_create_account_button()
        account_page = AccountPage(browser)
        account_page.success_message_should_be_present()

    def test_new_user_data_should_be_consistent(self, browser, user):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user)
        create_account_page.click_create_account_button()
        account_page = AccountPage(browser)
        account_page.new_user_data_should_be_consistent(user)


@pytest.mark.create_user_validations
class TestCreateUserValidations:
    @pytest.mark.parametrize("skip_field_name", CreateAccountPage.FIELD_NAMES)
    def test_create_account_without_required_field_should_cause_error_message(self, browser, user, skip_field_name):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user)
        create_account_page.clear_field(skip_field_name)
        create_account_page.click_create_account_button()
        create_account_page.error_message_and_invalid_marker_should_be_present(skip_field_name)

    def test_creation_new_account_with_same_email_should_be_prohibited(self, browser, user_data):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user_data)
        create_account_page.click_create_account_button()

        account_page = AccountPage(browser)
        account_page.sign_out()

        create_account_page.open(CREATE_ACCOUNT_LINK)
        create_account_page.enter_user_account_data(user_data)
        create_account_page.click_create_account_button()
        create_account_page.same_user_error_message_should_be_present()
