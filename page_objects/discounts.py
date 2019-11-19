import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Discounts():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def select_all_discounts(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[id="own_home"]')))
        self.select_discount_card('own_home').click()
        self.select_discount_card('has_job').click()
        self.select_discount_card('is_military').click()
        self.select_discount_card('is_aaa_member').click()
        self.select_discount_card('is_student').click()
        self.discount_continue_button().click()

    def select_all_discounts_except_student(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[id="own_home"]')))
        self.select_discount_card('own_home').click()
        self.select_discount_card('has_job').click()
        self.select_discount_card('is_military').click()
        self.select_discount_card('is_aaa_member').click()
        self.discount_continue_button().click()

    def select_discount_card(self, discount):
        discount_type = self.driver.find_element_by_css_selector('a[id="'+discount+'"]')
        return discount_type

    def discount_continue_button(self):
        continue_button = self.driver.find_element_by_css_selector('.cta-two .discount-info-cta-btn')
        return continue_button