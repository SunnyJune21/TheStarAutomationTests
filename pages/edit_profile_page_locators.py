from selenium.webdriver.common.by import By

class EditProfilePageLocators:
    PROFILE_FORM_ELEMENT = (By.ID, "profile-form")
    EMAIL_TEXT_FIELD = (By.ID, "email")
    POSTAL_CODE_FIELD = (By.ID, "input-postcode")
    PHONE_FIELD = (By.ID, "input-phone")
    COUNTRY = (By.ID, "select-country")
    SAVE_PROFILE_BTN = (By.XPATH, "//*[@id='profile-form']/div[3]/div/input")
    EDIT_SUCCESS_ELEMENT = (By.XPATH, "//*[@id='user-main-menu-wrapper']/div/div[1]/div[2]")
