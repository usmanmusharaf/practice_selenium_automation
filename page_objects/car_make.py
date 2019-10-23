from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.helper import Helper


class CarMake():

    def __init__(self, driver):
        self.driver = driver
        self.helper = Helper()
        self.wait = WebDriverWait(self.driver, 15)

    def select_car(self):
        self.wait.until(self.car_label_is_present())
        self.get_car_year('2014').click()
        self.wait.until(self.car_label_is_present())
        self.get_car_make('Honda').click()
        self.wait.until(self.car_label_is_present())
        self.get_car_model('Civic').click()
        self.wait.until(self.car_label_is_present())
        self.get_car_trim('Hybrid').click()

    def get_car_year(self, make_year):
        car_year = self.driver.find_elements_by_css_selector('.tt-dataset-car_year div')
        for year in car_year:
            if year.text == make_year:
                return year

    def get_car_make(self, make_company):
        car_make = self.driver.find_elements_by_css_selector('.tt-dataset-car_make span')
        for make in car_make:
            if make.text == make_company:
                return make

    def get_car_model(self, make_model):
        car_model = self.driver.find_elements_by_css_selector('.tt-dataset-model_year div')
        for model in car_model:
            if model.text == make_model:
                return model

    def get_car_trim(self, make_trim):
        car_trim = self.driver.find_elements_by_css_selector('.tt-dataset-car_trim div')
        for trim in car_trim:
            if trim.text == make_trim:
                return trim

    def car_label_is_present(self):
        return EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-label'))
