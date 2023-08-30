from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class LoginSuccessPage(BasePage):

    def get_username_label(self):
        lbl_username_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGIN_SUCCESS_USERNAME).text
        return lbl_username_txt

    def wait_and_click_menu_options(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.USER_MENU).click()

    def wait_and_click_sign_out(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.SIGN_OUT_BTN).click()

    def wait_and_click_manage_profile(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.MANAGE_PROFILE_BTN).click()
