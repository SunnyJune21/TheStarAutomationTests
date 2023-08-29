from selenium.webdriver.common.by import By


class RegisterPageLocators:

    EMAIL_TEXT_BOX = (By.ID, "input-email")
    POSTAL_CODE_TEXT_BOX = (By.ID, "input-postcode")
    FIRST_NAME_TEXT_BOX = (By.ID, "input-firstname")
    LAST_NAME_TEXT_BOX = (By.ID, "input-lastname")
    PASSWORD_TEXT_BOX = (By.ID, "input-password")
    CONFIRM_PASSWORD_TEXT_BOX = (By.ID, "input-confirm-password")
    CAPTCHA_CHECKBOX = (By.CLASS_NAME, "recaptcha-checkbox-border")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='user-register-form']/div[7]/div/button")