from selenium.webdriver.common.by import By


class CheckoutPage:

    country_loc = (By.XPATH, "//select")
    checkBox_loc = (By.CLASS_NAME, "chkAgree")
    proceedButton_loc = (By.XPATH, "//button[text()='Proceed']")



    def __init__(self, driver):
        self.driver = driver

    def country_CheckoutPage(self):
        return self.driver.find_element(*CheckoutPage.country_loc)

    def checkBox_CheckoutPage(self):
        return self.driver.find_element(*CheckoutPage.checkBox_loc)

    def proceedButton_CheckoutPage(self):
        return self.driver.find_element(*CheckoutPage.proceedButton_loc)

