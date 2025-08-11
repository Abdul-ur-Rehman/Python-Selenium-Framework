from selenium.webdriver import ActionChains

from Project1_ProtoCommerce_PSF.pageObjects.HomePage import HomePage
from Project1_ProtoCommerce_PSF.utilities.BaseClass import BaseClass


class Test_ProtoCommerce(BaseClass):


    def test_e2e_ProtoCommerce(self):
        self.driver.implicitly_wait(4)
        log = self.getLogger()
        homePage = HomePage(self.driver)

        productsPage = homePage.shopItems() #Click shop button on home page
        log.info("Moving to shop page from home page")
        products = productsPage.productsCadsInfo()
        log.info("Getting the details of products cards")


        for product in products:
            product_title = productsPage.extractProdcutTitle(product).text
            log.info(product_title)
            if product_title == "Blackberry":
                productsPage.cartButton(product).click() #Click add to cart button of the product

        checkoutPage1 = productsPage.checkoutButton() #Click checkout button on products page
        checkoutPage2 = checkoutPage1.checkoutButton_COP() #Click checkout button on checkout page 1
        checkoutPage2.locationTextbox().send_keys("pa") #Enter pa in the location text box on checkout page 2
        log.info("Sending country text as pa")

        self.verifyLinkPresence("Pakistan")

        action = ActionChains(self.driver)
        action.move_to_element(checkoutPage2.countrySelection()).click().perform() #Country selection from the dropdown list on checkout page 2

        checkoutPage2.checkboxMarker().click()  #Click on checkbox marker on checkout page 2
        checkoutPage2.purchaseButton().click() #Click on purchase button on checkout page 2
        success_message = checkoutPage2.successMessage().text
        log.info("Message coming from application is " + success_message)

        assert "Success! Thank you!" in success_message


