from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SaveQuote:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.long_wait = WebDriverWait(self.driver, 80)

    def fill_up_save_quote_form(self, email_id, phone_no, garaging_address):
        self.enter_email_id().send_keys(email_id)
        self.enter_phone_number().send_keys(phone_no)
        self.enter_garaging_address().send_keys(garaging_address)
        self.get_quote_button().click()
        self.check_quotes_load_properly()

    def enter_email_id(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="save_quote_email"]')))
        email_input = self.driver.find_element_by_css_selector('input[id="save_quote_email"]')
        return email_input

    def enter_phone_number(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="insured_phone"]')))
        phone_input = self.driver.find_element_by_css_selector('input[id="insured_phone"]')
        return phone_input

    def enter_garaging_address(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="address_street"]')))
        garaging_address = self.driver.find_element_by_css_selector('input[id="address_street"]')
        return garaging_address

    def assert_progress_end(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[id="headsup"] span'),'Comparing quotes is fast and easy with Insurify!'))

    def get_quote_button(self):
        self.long_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="save_quote_save_button"]')))
        get_quotes_btn = self.driver.find_element_by_css_selector('button[id="save_quote_save_button"]')
        return get_quotes_btn

    def check_quotes_load_properly(self):
        try:
            self.long_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.progress-bar-loader div[style="width: 100%;"]')))
        except TimeoutError:
            print('Loading took too much time !')
