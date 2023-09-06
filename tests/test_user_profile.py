
from pages.edit_profile_page import EditProfilePage
from pages.login_success_page import LoginSuccessPage
from pages.index_page import IndexPage
from pages.manage_profile_page import ManageProfilePage
from pages.sign_in_page import SignInPage
from resources.constants import TEST_SITE_URL


class TestUserProfile:

    # Test Case 6: verify that user can enter the "edit profile" page
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

# Test Case 7: verify that the email is correct
    def test_verify_email_in_edit_profile(self, driver, get_existing_credentials):
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
        displayed_email_text = edit_profile_page_ref.get_email_text()
        credentials = get_existing_credentials
        registered_email_text = credentials[0]

        assert displayed_email_text == registered_email_text, f"Email mismatch! Expected: {registered_email_text}, " \
                                                              f"Actual: {displayed_email_text}"

# Test Case 8: verify that the postal code is correct
    def test_verify_postal_code_in_edit_profile(self, driver, get_existing_credentials):
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
        displayed_postal_code_text = edit_profile_page_ref.get_postal_code_text()
        credentials = get_existing_credentials
        registered_postal_code_text = credentials[3]

        assert displayed_postal_code_text == registered_postal_code_text, f"Email mismatch! Expected: {registered_postal_code_text}, " \
                                                                          f"Actual: {displayed_postal_code_text}"

# Test Case 9: Editing user profile
    def test_enter_user_details(self, driver, get_existing_credentials):
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
        edit_profile_page_ref.wait_and_enter_phone(get_existing_credentials)
        edit_profile_page_ref.wait_and_enter_country(get_existing_credentials)
        edit_profile_page_ref.wait_and_click_save_profile()
        edit_success_element = edit_profile_page_ref.get_edit_success_element()

        assert edit_success_element is not None, "Editing is not successful"


