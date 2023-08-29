from pages.base_page import BasePage
from pages.register_page_locators import RegisterPageLocators
from resources.constants import MAX_WAIT_INTERVAL
import builtins


def get_user_input(prompt=""):
    if hasattr(builtins, "__pytestcapture__"):
        # Running under pytest capture mode
        return ""
    return input(prompt)

class RegisterPage(BasePage):

    def wait_and_type_email(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.EMAIL_TEXT_BOX).send_keys(
            usr_and_pw[0])

    def type_postal(self, usr_and_pw):
        self.find_element(RegisterPageLocators.POSTAL_CODE_TEXT_BOX).send_keys(
            usr_and_pw[1])

    def type_first_name(self, usr_and_pw):
        self.find_element(RegisterPageLocators.FIRST_NAME_TEXT_BOX).send_keys(
            usr_and_pw[2])

    def type_last_name(self, usr_and_pw):
        self.find_element(RegisterPageLocators.LAST_NAME_TEXT_BOX).send_keys(
            usr_and_pw[3])

    def type_password(self, usr_and_pw):
        self.find_element(RegisterPageLocators.PASSWORD_TEXT_BOX).send_keys(
            usr_and_pw[4])

    def type_confirm_password(self, usr_and_pw):
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_TEXT_BOX).send_keys(
            usr_and_pw[4])

    def captcha_checkbox(self):
        print("Manual intervention required. Press Enter to continue...")
        get_user_input()

    def click_create_account_btn(self):
        self.find_element(RegisterPageLocators.CREATE_ACCOUNT_BUTTON).click()

