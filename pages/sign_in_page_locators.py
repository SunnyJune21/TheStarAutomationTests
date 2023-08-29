from selenium.webdriver.common.by import By


class SignInPageLocators:

    CREATE_ACCOUNT_LINK = (By.XPATH, "//*[@id='main-page-container']/section/div[2]/div[2]/div[2]/a")
    EMAIL_SIGN_IN_FIELD = (By.ID, "user-username")
    PASSWORD_SIGN_IN_FIELD = (By.ID, "user-password")
    SIGN_IN_BTN = (By.CLASS_NAME, "btn btn-primary btn-full-xs")