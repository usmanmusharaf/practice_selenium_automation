import time
import unittest
from selenium import webdriver

from page_objects.add_incident import AddIncident
from page_objects.car_detail import CarDetails
from page_objects.car_make import CarMake
from page_objects.discounts import Discounts
from page_objects.driver_info import DriverInfo
from page_objects.driver_summary import DriverSummary
from page_objects.homepage import HomePage
from page_objects.prior_insurance import PriorInsurance
from page_objects.professional_discount import ProfessionalDiscount
from page_objects.save_quote import SaveQuote
from page_objects.student_discount import StudentDiscount


class CoreFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://insurify.com")
        self.assertIn("Insurify® - Official Site: Compare Insurance Quotes with Insurify", self.driver.title)

        self.homepage = HomePage(self.driver)
        self.car_make = CarMake(self.driver)
        self.car_detail = CarDetails(self.driver)
        self.driver_info = DriverInfo(self.driver)
        self.discounts = Discounts(self.driver)
        self.prior_insurance = PriorInsurance(self.driver)
        self.professional_discount = ProfessionalDiscount(self.driver)
        self.add_incident = AddIncident(self.driver)
        self.driver_summary = DriverSummary(self.driver)
        self.save_quote = SaveQuote(self.driver)
        self.student_discount = StudentDiscount(self.driver)

    def test_flow_in_ca_state(self):
        '''insurify_happy_flow_in_california'''
        self.homepage.enter_zipcode_and_proceed('90001')
        self.car_make.select_car()
        self.car_detail.select_car_details()
        self.driver_info.enter_driver_info('CA')
        self.discounts.select_all_discounts()
        self.prior_insurance.select_prior_insurance('yes', 'Esurance', 'March, 2020', '13')
        self.student_discount.select_student_options()
        self.professional_discount.enter_professional_information()
        self.add_incident.add_incident()
        self.driver_summary.select_driver_summary_options()
        self.save_quote.fill_up_save_quote_form('test.carmine@gmail.com', '9999999999', '599 Gresham Ave')

    def test_flow_in_il_state(self):
        '''insurify_happy_flow_in_illinois'''
        self.homepage.enter_zipcode_and_proceed('60007')
        self.car_make.select_car()
        self.car_detail.select_car_details()
        self.driver_info.enter_driver_info('IL')
        self.discounts.select_all_discounts_except_student()
        self.prior_insurance.select_no_prior_insurance()
        self.professional_discount.enter_professional_information()
        self.add_incident.add_incident()
        self.driver_summary.select_driver_summary_options()
        self.save_quote.fill_up_save_quote_form('test.carmine@gmail.com', '9999999999', '855 Spring Creek Ct Unit A')


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
