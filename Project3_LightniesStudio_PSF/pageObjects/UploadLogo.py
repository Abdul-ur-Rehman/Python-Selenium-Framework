
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions as EC


class UploadLogoPage:

    #Locators
    fullName_loc = (By.ID, "wpforms-13512-field_1")
    email_loc = (By.ID, "wpforms-13512-field_2")
    country_loc = (By.CLASS_NAME, "iti__country-container")
    flag_loc = (By.XPATH, "//span[text()='Pakistan']")
    phone_loc = (By.ID, "wpforms-13512-field_3")
    budgetDropdown_loc = (By.CSS_SELECTOR, ".choices__list.choices__list--single")
    budgetIdeaText_loc = (By.XPATH, "//option[text()='$650 - $1000']")

    def __init__(self, driver):
        self.driver = driver

    def enter_fullName(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.fullName_loc)).send_keys(name)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.email_loc)).send_keys(email)

    def countryFlag(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.country_loc)).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.flag_loc)).click()

    def enter_phone(self, phone):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.phone_loc)).send_keys(phone)

    def select_budget(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.budgetDropdown_loc)).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.budgetIdeaText_loc)).click()


