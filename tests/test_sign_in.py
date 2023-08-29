from pages import login_success_page
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

        username_lbl = login_success_page.get_username_label()
        assert username_lbl.__contains__(get_existing_credentials[2]), "User login failed!"

    def test_sign_out_existing_user(self, driver):
        login_success_page.wait_and_click_menu_options()
        login_success_page.wait_and_click_sign_out()

        username_lbl = login_success_page.get_username_label()
        assert username_lbl.__contains__("Sign In"), "User login failed!"

