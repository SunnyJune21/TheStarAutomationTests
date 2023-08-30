from pages.edit_profile_page import EditProfilePage
from pages.login_success_page import LoginSuccessPage
from pages.index_page import IndexPage
from pages.manage_profile_page import ManageProfilePage
from pages.sign_in_page import SignInPage
from resources.constants import TEST_SITE_URL


class TestUserProfile:

    def test_access_user_profile(self, driver, get_existing_credentials):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_sign_in_button()

        sign_in_page = SignInPage(driver)
        sign_in_page.wait_and_sign_in_email(get_existing_credentials)
        sign_in_page.wait_and_sign_in_password(get_existing_credentials)
        sign_in_page.wait_and_click_sign_in()

        login_success_page_ref = LoginSuccessPage(driver)
        login_success_page_ref.wait_and_click_menu_options()
        login_success_page_ref.wait_and_click_manage_profile()

        manage_profile_page_ref = ManageProfilePage(driver)
        manage_profile_page_ref.wait_and_click_user_account_btn()

        edit_profile_page_ref = EditProfilePage(driver)
        edit_profile_form_element = edit_profile_page_ref.get_edit_profile_form_element()
        assert edit_profile_form_element is not None, "Edit profile element is not found"
