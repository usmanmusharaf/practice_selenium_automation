from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DriverSummary:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def select_driver_summary_options(self):
        self.continue_button().click()

    def continue_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ens-discount-summary-continue')))
        continue_btn = self.driver.find_element_by_css_selector('.ens-discount-summary-continue')
        return continue_btn