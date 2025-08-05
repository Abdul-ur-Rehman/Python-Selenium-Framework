from selenium.webdriver.common.by import By

from Project2_GreenKart_PSF.pageObjects.CheckoutPage import CheckoutPage


class DiscountPage:

    tablePrices_loc = (By.CSS_SELECTOR, "tr td:nth-child(5) p")
    totalAmount_loc = (By.CLASS_NAME, "totAmt")
    promoCodeTextBox_loc = (By.CLASS_NAME, "promoCode")
    promoCodeButton_loc = (By.CLASS_NAME, "promoBtn")
    discountAmount_loc = (By.CLASS_NAME, "discountAmt")
    placeOrderButton_loc = (By.XPATH, "//button[text()='Place Order']")



    def __init__(self, driver):
        self.driver = driver

    def tablePrices_DiscountPage(self):
        return self.driver.find_elements(*DiscountPage.tablePrices_loc)

    def totalAmount_DiscountPage(self):
        return self.driver.find_element(*DiscountPage.totalAmount_loc)

    def promoCodeTextBox_DiscountPage(self):
        return self.driver.find_element(*DiscountPage.promoCodeTextBox_loc)

    def promoCodeButton_DiscountPage(self):
        return self.driver.find_element(*DiscountPage.promoCodeButton_loc)

    def discountAmount_DiscountPage(self):
        return self.driver.find_element(*DiscountPage.discountAmount_loc)

    def placeOrderButton_DiscountPage(self):
        self.driver.find_element(*DiscountPage.placeOrderButton_loc).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
