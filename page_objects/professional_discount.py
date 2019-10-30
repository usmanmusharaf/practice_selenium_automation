from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ProfessionalDiscount:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def enter_professional_information(self):
        self.select_industry('Construction / Energy / Mining').click()
        self.select_occupation('Construction-Project Manager').click()
        self.continue_button().click()

    def select_industry(self, industry_text):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label')))
        industry_list = self.driver.find_elements_by_css_selector('.tt-dataset-industry div')
        for industry in industry_list:
            if industry.text == industry_text:
                return industry

    def select_occupation(self, occupation_text):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label')))
        occupation_list = self.driver.find_elements_by_css_selector(' .tt-dataset-occupation div')
        for occupation in occupation_list:
            if occupation.text == occupation_text:
                return occupation

    def continue_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="professional_discount_continue_button"]')))
        continue_btn = self.driver.find_element_by_css_selector('button[id="professional_discount_continue_button"]')
        return continue_btn