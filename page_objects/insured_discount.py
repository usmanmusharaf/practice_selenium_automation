from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InsuredDiscount:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.short_wait = WebDriverWait(self.driver, 5)

    def select_prior_insurance(self, insured_status, prior_carrier, month_and_year, date_expire):

        try:
            self.check_shopping_frequency_survey()
            self.select_shopping_frequency_survey().click()
        except:
            pass

        self.select_currently_insured_status(insured_status).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label')))
        self.select_prior_carrier(prior_carrier).click()
        self.select_month_year(month_and_year).click()
        self.select_date(date_expire).click()
        self.select_insured_duration('3-4 years').click()
        try:
            self.check_current_premium_experiment()
            self.select_current_premium_bi().click()
            self.select_current_premium_deductibles().click()
        except:
            pass

        self.insured_continue_button().click()

    def select_no_prior_insurance(self):

        try:
            self.check_shopping_frequency_survey()
            self.select_shopping_frequency_survey().click()
        except:
            pass

        self.select_currently_insured_status("no").click()
        self.select_not_insured_reason('car_in_storage').click()
        self.select_last_insured_period().click()
        self.not_insured_continued_button().click()

    def check_shopping_frequency_survey(self):
        self.short_wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[data-analytics-label="first_time_insurer"]')))

    def select_shopping_frequency_survey(self):
        shopping_survey = self.driver.find_element_by_css_selector('label[data-analytics-label="first_time_insurer"]')
        return shopping_survey

    def select_currently_insured_status(self, status):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-analytics-label="yes"]')))
        insured_status = self.driver.find_element_by_css_selector('label[data-analytics-label="' + status + '"]')
        return insured_status

    def select_prior_carrier(self, prior_carrier):
        carriers = self.driver.find_elements_by_css_selector('.tt-dataset-carrier span')
        for carrier in carriers:
            if carrier.text == prior_carrier:
                return carrier

    def select_month_year(self, month_and_year):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label')))
        month_years = self.driver.find_elements_by_css_selector('.tt-selectable')
        for month_year in month_years:
            if month_year.text == month_and_year:
                return month_year

    def select_date(self, date_expire):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label')))
        date_list = self.driver.find_elements_by_css_selector('.tt-selectable')
        for date in date_list:
            if date.text == date_expire:
                return date

    def select_insured_duration(self, duration_option):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="insured_discount_insured_months_0"]')))
        insured_duration = self.driver.find_elements_by_css_selector('div[id="prior_coverage_insured_months"] label')
        for duration in insured_duration:
            if duration.text == duration_option:
                return duration

    def select_not_insured_reason(self, reason):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-analytics-label="car_in_storage"]')))
        lapse_reason = self.driver.find_element_by_css_selector('label[data-analytics-label="' + reason + '"]')
        return lapse_reason

    def select_last_insured_period(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-analytics-label="15"]')))
        insured_lapse = self.driver.find_element_by_css_selector('label[data-analytics-label="15"]')
        return insured_lapse

    def insured_continue_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="insured_discount_continue_button"]')))
        continue_btn = self.driver.find_element_by_css_selector('button[id="insured_discount_continue_button"]')
        return continue_btn

    def not_insured_continued_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="continue_button"]')))
        continue_btn = self.driver.find_element_by_css_selector('button[id="continue_button"]')
        return continue_btn

    def check_current_premium_experiment(self):
        self.short_wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div[id="insured_discount_current_coverage_bi"] label[data-analytics-label="15,30"]')))

    def select_current_premium_bi(self):
        current_premium_bi = self.driver.find_element_by_css_selector(
            'div[id="insured_discount_current_coverage_bi"] label[data-analytics-label="15,30"]')
        return current_premium_bi

    def select_current_premium_deductibles(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div[id="insured_discount_current_deductibles"] label[data-analytics-label="500,500"]')))

        current_premium_deductible = self.driver.find_element_by_css_selector(
            'div[id="insured_discount_current_deductibles"] label[data-analytics-label="500,500"]')
        return current_premium_deductible
