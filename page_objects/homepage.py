from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.helper import Helper


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        # page_objects
        self.helper = Helper(self.driver)

    def enter_zipcode_and_proceed(self, zipcode):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="intercom-container"]')))
        # enter zipcode
        zipcode_input = self.driver.find_element_by_css_selector('div[class="flex-row"] input[id="zipcode_input"]')
        zipcode_input.clear()
        zipcode_input.send_keys(zipcode)

        # click on zipcode button on homepage
        homepage_button = self.driver.find_element_by_css_selector('button[id="main-auto-zipcode-button"]')
        homepage_button.click()
