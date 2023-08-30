from pages.base_page import BasePage
from pages.manage_profile_page_locators import ManageProfilePageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ManageProfilePage(BasePage):

    def wait_and_click_user_account_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ManageProfilePageLocators.USER_ACCOUNT_BTN).click()