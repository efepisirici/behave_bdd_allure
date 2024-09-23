from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from features.pages.base_page import *
from features.pages.base_page import BasePage

class AppointmentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    APPOINTMENT_BUTTON = (By.ID, 'btn-make-appointment')
    FACILITY_DROP_DOWN = (By.ID, 'combo_facility')
    HOSPITAL_READMISSION = (By.XPATH,'//label[normalize-space()="Apply for hospital readmission"]')
    HEALTHCARE_PROGRAM = (By.XPATH, '//input[@id="radio_program_medicaid"]')
    VIST_DATE = (By.XPATH, '//input[@id="txt_visit_date"]')
    COMMENT = (By.XPATH, '//textarea[@id="txt_comment"]')
    BOOK_APPOINTMENT = (By.ID, 'btn-book-appointment')

    def click_appointment_button(self):
        appointment_button = self.find_element(self.APPOINTMENT_BUTTON)
        appointment_button.click()

    def verify_appointment_page_displayed(self):
        try:
          appoint_button =   self.find_elements(self.APPOINTMENT_BUTTON)
          return appoint_button.displayed()
        except:
          return False

        # to select based on options displayed text
    def select_a_facility_by_txt(self, facility_txt):
        facility_dropdown = self.find_element(self.FACILITY_DROP_DOWN)
        select = Select(facility_dropdown)
        select.select_by_visible_text(facility_txt)

         # to select based on options by its value attribute
    def select_a_facility_by_value(self, facility_option_value):
        facility_dropdown = self.find_element(self.FACILITY_DROP_DOWN)
        select = Select(facility_dropdown)
        select.select_by_value(facility_option_value)

    def select_hospital_readmission(self):
        self.click_from_base(self.HOSPITAL_READMISSION)

    def select_hospital_program(self):
        self.click_from_base(self.HEALTHCARE_PROGRAM)

    def select_visit_date(self, date_value):
        self.send_keys_from_base(self.VIST_DATE, date_value)

    def enter_comment(self, comment_text):
        self.send_keys_from_base(self.COMMENT, comment_text)

    def click_book_appointment_button(self):
        self.click_from_base(self.BOOK_APPOINTMENT)




