from test_utils import *
from pages.sign_in_page import SignInPage
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    def test_register_new_user(self, driver, get_new_user_credentials):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_click_create_account_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_email(get_new_user_credentials)
        register_page.type_postal(get_new_user_credentials)
        register_page.type_first_name(get_new_user_credentials)
        register_page.type_last_name(get_new_user_credentials)
        register_page.type_password(get_new_user_credentials)
        register_page.type_confirm_password(get_new_user_credentials)
        register_page.captcha_checkbox()
        register_page.click_create_account_btn()

        register_success_page = RegisterSuccessPage(driver)
        login_lbl = register_success_page.get_login_label()
        assert login_lbl.__contains__(get_new_user_credentials[2]), "User registration failed!"