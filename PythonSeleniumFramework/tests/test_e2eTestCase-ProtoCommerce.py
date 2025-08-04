from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PythonSeleniumFramework.pageObjects.HomePage import HomePage
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e_ProtoCommerce(self, setup):
        self.driver.implicitly_wait(4)
        homePage = HomePage(self.driver)

        productsPage = homePage.shopItems() #Click shop button on home page
        products = productsPage.productsCadsInfo()

        for product in products:
            if productsPage.extractProdcutTitle(product).text == "Blackberry":
                productsPage.cartButton(product).click() #Click add to cart button of the product

        checkoutPage1 = productsPage.checkoutButton() #Click checkout button on products page
        checkoutPage2 = checkoutPage1.checkoutButton_COP() #Click checkout button on checkout page 1
        checkoutPage2.locationTextbox().send_keys("pa") #Enter pa in the location text box on checkout page 2

        self.verifyLinkPresence("Pakistan")

        action = ActionChains(self.driver)
        action.move_to_element(checkoutPage2.countrySelection()).click().perform() #Country selection from the dropdown list on checkout page 2

        checkoutPage2.checkboxMarker().click()  #Click on checkbox marker on checkout page 2
        checkoutPage2.purchaseButton().click() #Click on purchase button on checkout page 2

        assert "Success! Thank you!" in self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        print(checkoutPage2.successMessage().text)

