from pages.invalid_credentials_page import InvalidCredentialsPage
from pages.login_success_page import LoginSuccessPage
from pages.index_page import IndexPage
from pages.sign_in_page import SignInPage
from resources.constants import TEST_SITE_URL


class TestSignIn:

    def test_sign_in_existing_user(self, driver, get_existing_credentials):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_sign_in_email(get_existing_credentials)
        sign_in_page.wait_and_sign_in_password(get_existing_credentials)
        sign_in_page.wait_and_click_sign_in()

        login_success_page_ref = LoginSuccessPage(driver)
        username_lbl = login_success_page_ref.get_username_label()
        assert username_lbl.__contains__(get_existing_credentials[2]), "User login failed!"

    def test_sign_out_existing_user(self, driver, get_existing_credentials):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_sign_in_email(get_existing_credentials)
        sign_in_page.wait_and_sign_in_password(get_existing_credentials)
        sign_in_page.wait_and_click_sign_in()

        login_success_page_ref = LoginSuccessPage(driver)
        login_success_page_ref.wait_and_click_menu_options()
        login_success_page_ref.wait_and_click_sign_out()

        username_lbl = login_success_page_ref.get_username_label()
        assert username_lbl.__contains__("Sign In"), "User login failed!"

    def test_sign_in_wrong_password(self, driver, sign_in_with_wrong_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_sign_in_email(sign_in_with_wrong_password)
        sign_in_page.wait_and_sign_in_password(sign_in_with_wrong_password)
        sign_in_page.wait_and_click_sign_in()

        invalid_credentials_page_ref = InvalidCredentialsPage(driver)
        wrong_password_msg = invalid_credentials_page_ref.get_error_msg()
        assert wrong_password_msg is not None, "Error message element is not found"

    def test_sign_in_wrong_email(self, driver, sign_in_with_wrong_email):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_sign_in_email(sign_in_with_wrong_email)
        sign_in_page.wait_and_sign_in_password(sign_in_with_wrong_email)
        sign_in_page.wait_and_click_sign_in()

        invalid_credentials_page_ref = InvalidCredentialsPage(driver)
        wrong_password_msg = invalid_credentials_page_ref.get_error_msg()
        assert wrong_password_msg is not None, "Error message element is not found"
