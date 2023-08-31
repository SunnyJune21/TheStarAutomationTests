from selenium.webdriver.common.by import By

class EditProfilePageLocators:
    PROFILE_FORM_ELEMENT = (By.ID, "profile-form")
    EMAIL_TEXT_FIELD = (By.ID, "email")
    POSTAL_CODE_FIELD = (By.ID, "input-postcode")