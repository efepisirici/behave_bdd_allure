from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(exp.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(exp.presence_of_all_elements_located(locator))

    def go_to(self, url):
        self.driver.get(url)

    def click_from_base(self, locator):
        self.find_element(locator).click()

    def send_keys_from_base(self, locator, value):
        self.find_element(locator).send_keys(value)
