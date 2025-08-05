from Project2_GreenKart_PSF.pageObjects.HomePage import HomePage
from Project2_GreenKart_PSF.testData.HomePageTestData import HomePageTestData
from Project2_GreenKart_PSF.utilities.BaseClass import BaseClass


class Test_GreenKart(BaseClass):

    extracted_list = []
    test_data = HomePageTestData()

    def test_e2e_GreenKart(self, setup):
        self.driver.implicitly_wait(4)
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.searchBar_HomePage().send_keys("ca")
        log.info("Enter 'ca' in the search bar")

        products = homePage.productCards_HomePage()


        assert len(products) > 0

        log.info("Extracting products title")
        for product in products:
            self.extracted_list.append(homePage.productTitle_HomePage(product).text)
            log.info(homePage.productTitle_HomePage(product).text)
            homePage.productCartButton_HomePage(product).click()
        log.info("Products added to cart")

        #Validation that extracted and existed lists are same
        assert self.test_data.existed_list == self.extracted_list

        homePage.cartButtonHeader_HomePage().click()
        discountPage = homePage.checkoutButtonHeader_HomePage()
        log.info("Moved to discount page")

        #Validation that Sum of all products in the table is same as the total of all the products shown
        actual_Total = 0
        prices = discountPage.tablePrices_DiscountPage()

        for price in prices:
            actual_Total = actual_Total + int(price.text)

        total_Amount = int(discountPage.totalAmount_DiscountPage().text)

        assert actual_Total == total_Amount

        discountPage.promoCodeTextBox_DiscountPage().send_keys("rahulshettyacademy")
        discountPage.promoCodeButton_DiscountPage().click()
        log.info("Discount code applied")

        self.verifyLinkPresence("Code applied ..!")
        log.info("Discount code verified")

        #Validation that discount price is less than the total amount

        discount_Amt = float(discountPage.discountAmount_DiscountPage().text)

        assert discount_Amt < total_Amount

        checkoutPage = discountPage.placeOrderButton_DiscountPage()
        log.info("Moved to checkout page")

        self.selectCountry(checkoutPage.country_CheckoutPage(), "Pakistan")

        checkoutPage.checkBox_CheckoutPage().click()
        checkoutPage.proceedButton_CheckoutPage().click()
        log.info("Order placed!")




