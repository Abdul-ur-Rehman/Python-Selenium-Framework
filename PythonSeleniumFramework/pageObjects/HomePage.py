from selenium.webdriver.common.by import By

from PythonSeleniumFramework.pageObjects.ProductsPage import ProductsPage


class HomePage:

    shop_loc = (By.XPATH, "//a[text()='Shop']")

    name_form_loc = (By.NAME, "name")
    email_form_loc = (By.NAME, "email")
    password_form_loc = (By.ID, "exampleInputPassword1")
    checkbox_form_loc = (By.ID, "exampleCheck1")
    gender_form_loc = (By.ID, "exampleFormControlSelect1")
    radioButton_form_loc = (By.ID, "inlineRadio2")
    date_form_loc = (By.CSS_SELECTOR, "input[type='date']")
    submitButton_form_loc = (By.XPATH, "//input[@type='submit']")
    successMessage_form_loc = (By.CLASS_NAME, "alert-success")


    def __init__(self, driver):
        self.driver = driver


    def shopItems(self):

        self.driver.find_element(*HomePage.shop_loc).click()
        productsPage = ProductsPage(self.driver)
        return productsPage

    def nameForm(self):
        return self.driver.find_element(*HomePage.name_form_loc)

    def emailForm(self):
        return self.driver.find_element(*HomePage.email_form_loc)

    def passwordForm(self):
        return self.driver.find_element(*HomePage.password_form_loc)

    def checkboxForm(self):
        return self.driver.find_element(*HomePage.checkbox_form_loc)

    def genderForm(self):
        return self.driver.find_element(*HomePage.gender_form_loc)

    def radioButtonForm(self):
        return self.driver.find_element(*HomePage.radioButton_form_loc)

    def dateForm(self):
        return self.driver.find_element(*HomePage.date_form_loc)

    def submitButtonForm(self):
        return self.driver.find_element(*HomePage.submitButton_form_loc)

    def successMessageForm(self):
        return self.driver.find_element(*HomePage.successMessage_form_loc)