from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Project2_GreenKart_PSF.pageObjects.HomePage import HomePage
from Project2_GreenKart_PSF.utilities.BaseClass import BaseClass


class Test_GreenKart(BaseClass):

    existed_list = ["Cauliflower - 1 Kg", "Carrot - 1 Kg", "Capsicum", "Cashews - 1 Kg"]
    extracted_list = []

    def test_e2e_GreenKart(self, setup):
        self.driver.implicitly_wait(4)
        homePage = HomePage(self.driver)
        homePage.searchBar_HomePage().send_keys("ca")

        products = homePage.productCards_HomePage()
        #self.driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ca")
        #products = self.driver.find_elements(By.XPATH, "//div/div[@class='product']")

        assert len(products) > 0

        #Extract product titles
        for product in products:
            self.extracted_list.append(homePage.productTitle_HomePage(product).text)
            homePage.productCartButton_HomePage(product).click()

        #Validation that extracted and existed lists are same
        assert self.existed_list == self.extracted_list

        homePage.cartButtonHeader_HomePage().click()
        discountPage = homePage.checkoutButtonHeader_HomePage()

        #Validation that Sum of all products in the table is same as the total of all the products shown
        actual_Total = 0
        prices = discountPage.tablePrices_DiscountPage()

        for price in prices:
            actual_Total = actual_Total + int(price.text)

        total_Amount = int(discountPage.totalAmount_DiscountPage().text)

        assert actual_Total == total_Amount

        discountPage.promoCodeTextBox_DiscountPage().send_keys("rahulshettyacademy")
        discountPage.promoCodeButton_DiscountPage().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

        #Validation that discount price is less than the total amount

        discount_Amt = float(discountPage.discountAmount_DiscountPage().text)

        assert discount_Amt < total_Amount

        checkoutPage = discountPage.placeOrderButton_DiscountPage()

        select = Select(checkoutPage.country_CheckoutPage())
        select.select_by_visible_text("Pakistan")

        checkoutPage.checkBox_CheckoutPage().click()
        checkoutPage.proceedButton_CheckoutPage().click()


