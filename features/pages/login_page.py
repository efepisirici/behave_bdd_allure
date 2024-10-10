from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    LOGIN_INPUT = (By.XPATH, '//input[@id="txt-username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="txt-password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="btn-login"]')
    WRONG_LOGIN_MSG = (By.XPATH, '//p[@class="lead text-danger"]')

    def enter_username(self, username):
        try:
            login_field = self.find_element(self.LOGIN_INPUT)
            login_field.send_keys(username)
            return True
        except Exception:
            return False

    def enter_password(self, password):
        try:
            password_field = self.find_element(self.PASSWORD_INPUT)
            password_field.send_keys(password)
            return True
        except Exception:
            return False
    def click_submit(self):
        submit_button = self.find_element(self.SUBMIT_BUTTON)
        submit_button.click()

    def validation_msg_displayed(self):
        try:
            wrong_msg = self.find_element(self.WRONG_LOGIN_MSG)
            return wrong_msg.is_displayed()
        except Exception:
         return False
