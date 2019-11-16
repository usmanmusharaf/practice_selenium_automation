import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.helper import Helper

class StudentDiscount:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.helper = Helper()

    def select_student_options(self):
        self.check_page_load()
        self.enter_gpa().send_keys(4)
        self.continue_btn().click()

        time.sleep(5)

    def check_page_load(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.panel-header .normal'), 'You could qualify for a discount based on your GPA'))

    def enter_gpa(self):
        gpa_score = self.driver.find_element_by_css_selector('input[id="student_discount_gpa_input"]')
        return gpa_score

    def continue_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="student_discount_continue_button"]')))
        continue_button = self.driver.find_element_by_css_selector('button[id="student_discount_continue_button"]')
        return continue_button