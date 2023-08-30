from pages.base_page import BasePage
from pages.edit_profile_page_locators import EditProfilePageLocators
from resources.constants import MAX_WAIT_INTERVAL


class EditProfilePage(BasePage):

    def get_edit_profile_form_element(self):
        edit_profile_form = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, EditProfilePageLocators.PROFILE_FORM_ELEMENT)
        return edit_profile_form