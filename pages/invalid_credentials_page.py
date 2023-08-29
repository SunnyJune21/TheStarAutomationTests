from pages.base_page import BasePage
from pages.invalid_credentials_page_locators import InvalidCredentialsPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class InvalidCredentialsPage(BasePage):

    def get_error_msg(self):
        error_msg = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, InvalidCredentialsPageLocators.PASSWORD_ERROR_MSG)
        return error_msg
