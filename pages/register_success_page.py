from pages.base_page import BasePage
from pages.register_success_page_locators import RegisterSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class RegisterSuccessPage(BasePage):

    def get_login_label(self):
        lbl_login_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, RegisterSuccessPageLocators.LOGIN_LBL).text
        return lbl_login_txt
