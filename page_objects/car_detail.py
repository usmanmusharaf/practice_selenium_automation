from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.helper import Helper


class CarDetails:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        # page_objects
        self.helper = Helper(self.driver)

    def select_car_details(self):
        self.wait.until(self.card_to_be_clickable())
        self.select_car_usage('Commute to school').click()
        self.select_car_usage('Rideshare Driver').click()
        self.select_distance_each_way(10).click()
        self.select_payment_status('lean').click()
        self.select_deductible('full_coverage').click()
        self.save_and_continue_button().click()

    @staticmethod
    def assert_car_detail_form():
        return EC.presence_of_element_located((By.CSS_SELECTOR, 'form[id="car_details_form"]'))

    def select_car_usage(self, car_used_for):
        car_usage = self.driver.find_elements_by_css_selector('.absolute-checkbox span')
        for usage in car_usage:
            if usage.text == car_used_for:
                return usage

    def select_distance_each_way(self, value):
        distance = self.driver.find_element_by_css_selector(
            '.btn-group > label[data-field="mileage_per_day"]:nth-of-type(' + str(int(value / 5)) + ')')
        return distance

    @staticmethod
    def card_to_be_clickable():
        usage_assertion = EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[id="used_for_work"]'))
        return usage_assertion

    def select_payment_status(self, payment):
        payment_status = self.driver.find_element_by_css_selector(
            'label[for="car_details_payment_status_' + payment + '_radio"]')
        return payment_status

    def select_deductible(self, deductible_type):
        self.helper.assert_for_presence_of_element('label[data-field="deductibles"]:nth-child(1)')
        deductible = self.driver.find_element_by_css_selector('label[data-analytics-label="' + deductible_type + '"]')
        return deductible

    def save_and_continue_button(self):
        self.helper.assert_for_element_to_be_clickable('button[id="car_details_continue_to_driver"]')
        move_to_driver_button = self.driver.find_element_by_css_selector('button[id="car_details_continue_to_driver"]')
        return move_to_driver_button
