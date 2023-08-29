from pages.base_page import BasePage
from pages.sign_in_page_locators import SignInPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignInPage(BasePage):

    def wait_and_click_create_account_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.CREATE_ACCOUNT_LINK).click()

    def wait_and_sign_in_email(self, eml_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.EMAIL_SIGN_IN_FIELD).send_keys(
            eml_and_pw[0])

    def wait_and_sign_in_password(self, eml_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.PASSWORD_SIGN_IN_FIELD).send_keys(
            eml_and_pw[1])

    def wait_and_click_sign_in(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.SIGN_IN_BTN).click()