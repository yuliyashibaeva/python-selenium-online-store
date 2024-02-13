from pages.create_account_page import CreateAccountPage
from pages.account_page import AccountPage


class TestCreateNewUser:
    def test_new_user_should_be_created(self, browser, user_data):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CreateAccountPage.CREATE_ACCOUNT_LINK)
        create_account_page.create_new_account(user_data)
        account_page = AccountPage(browser)
        assert account_page.is_success_message_present(), \
            "A new user wasn't created: there is no success message on the account page"

    def test_new_user_data_should_be_consistent(self, browser, user_data):
        create_account_page = CreateAccountPage(browser)
        create_account_page.open(CreateAccountPage.CREATE_ACCOUNT_LINK)
        create_account_page.create_new_account(user_data)
        account_page = AccountPage(browser)
        user_contact_info = account_page.get_user_data().split("\n")

        assert (user_contact_info[0].strip() == user_data['full_name']
                and user_contact_info[1].strip() == user_data['user_email']), \
            (f"The account information isn't correct.\n"
             f"Received: user name '{user_contact_info[0].strip()}', user email '{user_contact_info[1].strip()}'.\n"
             f"Expected: user name '{user_data['full_name']}', user email '{user_data['user_email']}'.")

