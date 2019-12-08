from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.helper import Helper


class DriverInfo:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.helper = Helper(self.driver)

    def enter_driver_info(self, state_id):
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.is-current a[href="#/drivers/driver_summary"]')))
        self.enter_firstname().send_keys('Carmine')
        self.enter_lastname().send_keys('Falcone')
        self.enter_dob().send_keys(7777)
        self.select_gender('1').click()

        # for CA state
        if state_id == 'CA':
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'label[data-field="was_license_suspended"]:nth-of-type(1)')))
            self.select_license_status().click()
            self.select_license_age('18')
        else:
            pass

        # for CA state
        if state_id == 'CA':
            pass
        else:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-analytics-label="excellent"]')))
            self.select_credit_score('Good').click()
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-analytics-label="some_college_no_degree"]')))
        self.select_level_of_education('Doctoral').click()
        self.save_and_continue_button().click()

    def enter_firstname(self):
        firstname = self.driver.find_element_by_css_selector('input[name="first_name"]')
        return firstname

    def enter_lastname(self):
        lastname = self.driver.find_element_by_css_selector('input[id="last_name"]')
        return lastname

    def enter_dob(self):
        dob = self.driver.find_element_by_css_selector('input[id="driver_info_dob"]')
        return dob

    def select_gender(self, gender_type):
        gender = self.driver.find_element_by_css_selector('label[data-field="gender"]:nth-of-type(' + gender_type + ')')
        return gender

    def select_credit_score(self, credit_score):
        credit_scores = self.driver.find_elements_by_css_selector('label[data-field="credit_score"]')
        for credit in credit_scores:
            if credit.text == credit_score:
                return credit

    def select_level_of_education(self, education):
        education_level = self.driver.find_elements_by_css_selector('label[data-field="education"]')
        for edu in education_level:
            if edu.text == education:
                return edu

    def select_license_status(self):
        license_status = self.driver.find_element_by_css_selector(
            'label[data-field="was_license_suspended"]:nth-of-type(1)')
        return license_status

    def select_license_age(self, driver_license_age):
        license_age = self.driver.find_elements_by_css_selector('div[id="driver_info_license_age_container"] label')
        for age in license_age:
            if age.text == driver_license_age:
                return age

    def save_and_continue_button(self):
        driver_info_btn = self.driver.find_element_by_css_selector('button[id="driver_info_continue_btn"]')
        return driver_info_btn
