from selenium.webdriver.common.by import By


class CheckoutPage:

    checkooutButton_COP_loc = (By.CLASS_NAME, "btn-success")
    location_textbox_loc = (By.ID, "country")
    country_selection_loc = (By.XPATH, "//a[text()='Pakistan']")
    checkbox_marker_loc = (By.CSS_SELECTOR, ".checkbox")
    purchaseButton_loc = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_message_loc = (By.CSS_SELECTOR, ".alert-success")




    def __init__(self, driver):
        self.driver = driver


    def checkoutButton_COP(self):
        self.driver.find_element(*CheckoutPage.checkooutButton_COP_loc).click()
        checkoutPage2 = CheckoutPage(self.driver)
        return checkoutPage2

    def locationTextbox(self):
        return self.driver.find_element(*CheckoutPage.location_textbox_loc)

    def countrySelection(self):
        return self.driver.find_element(*CheckoutPage.country_selection_loc)

    def checkboxMarker(self):
        return self.driver.find_element(*CheckoutPage.checkbox_marker_loc)

    def purchaseButton(self):
        return self.driver.find_element(*CheckoutPage.purchaseButton_loc)

    def successMessage(self):
        return self.driver.find_element(*CheckoutPage.success_message_loc)