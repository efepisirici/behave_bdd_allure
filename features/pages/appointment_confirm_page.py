from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class AppointmentConfirm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    APPOINTMENT_CONFIRM_MSG = (By.XPATH,'//h2[normalize-space()="Appointment Confirmation"]')

    def verify_appointment_confirm_msg(self):
        try:
            confirm_msg = self.find_element(self.APPOINTMENT_CONFIRM_MSG)
            return confirm_msg.is_displayed()
        except:
            return False