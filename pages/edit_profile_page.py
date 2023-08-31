from pages.base_page import BasePage
from pages.edit_profile_page_locators import EditProfilePageLocators
from resources.constants import MAX_WAIT_INTERVAL


class EditProfilePage(BasePage):

    def get_edit_profile_form_element(self):
        edit_profile_form = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                  EditProfilePageLocators.PROFILE_FORM_ELEMENT)
        return edit_profile_form

    def get_email_text(self):
        email_text_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 EditProfilePageLocators.EMAIL_TEXT_FIELD)
        displayed_email = email_text_field.get_attribute("value")
        return displayed_email

    def get_postal_code_text(self):
        postal_code_text_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                       EditProfilePageLocators.POSTAL_CODE_FIELD)
        displayed_postal_code = postal_code_text_field.get_attribute("value")
        return displayed_postal_code
