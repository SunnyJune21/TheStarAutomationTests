from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_SUCCESS_USERNAME = (By.CLASS_NAME, "userName")
    USER_MENU = (By.CLASS_NAME, "tnt-svg tnt-chevron-down tnt-w-14 userPanelIndicator")
    SIGN_OUT_BTN = (By.CLASS_NAME, "dropdown-item logout-btn")