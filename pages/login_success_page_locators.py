from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_SUCCESS_USERNAME = (By.CLASS_NAME, "userName")
    USER_MENU = (By.XPATH, "//*[@id='userControlPanel-2841699']")
    SIGN_OUT_BTN = (By.XPATH, "//*[@id='logout-2841699']")
    MANAGE_PROFILE_BTN = (By.XPATH, "//*[@id='user-control-panel-2841699']/div/ul/li[2]/a")