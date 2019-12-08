from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Helper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def assert_for_presence_of_element(self, css_selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def assert_for_element_to_be_clickable(self, css_selector):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
