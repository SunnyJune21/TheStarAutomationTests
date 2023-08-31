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

    def wait_and_enter_phone(self, credentials):
        phone_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, EditProfilePageLocators.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(credentials[4])

    def wait_and_click_save_profile(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, EditProfilePageLocators.SAVE_PROFILE_BTN).click()

    def get_edit_success_element(self):
        edit_success_element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, EditProfilePageLocators.EDIT_SUCCESS_ELEMENT)
        return edit_success_element

