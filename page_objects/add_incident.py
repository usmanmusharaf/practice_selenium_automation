from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddIncident():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def add_incident(self):
        self.keep_going_btn().click()

    def keep_going_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[id="add_incidents_continue_button"]')))
        button = self.driver.find_element_by_css_selector('a[id="add_incidents_continue_button"]')
        return button

