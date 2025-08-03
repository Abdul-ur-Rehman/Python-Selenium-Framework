from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonSeleniumFramework.pageObjects.CheckoutPage import CheckoutPage
from PythonSeleniumFramework.pageObjects.HomePage import HomePage
from PythonSeleniumFramework.pageObjects.ProductsPage import ProductsPage
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e_ProtoCommerce(self, setup):
        self.driver.implicitly_wait(4)

        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        checkoutPage = CheckoutPage(self.driver)


        homePage.shopItems().click() #Click shop button on home page
        products = productsPage.productsCadsInfo()

        for product in products:
            if productsPage.extractProdcutTitle(product).text == "Blackberry":
                productsPage.cartButton(product).click() #Click add to carr button of the product

        productsPage.checkoutButton().click() #Click checkout button on products page
        checkoutPage.checkoutButton_COP().click() #Click checkout button on checkout page 1
        checkoutPage.locationTextbox().send_keys("pa") #Enter pa in the location text box on checkout page 2

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Pakistan']")))

        action = ActionChains(self.driver)
        action.move_to_element(checkoutPage.countrySelection()).click().perform() #Country selection from the dropdown list on checkout page 2

        checkoutPage.checkboxMarker().click()  #Click on checkbox marker on checkout page 2
        checkoutPage.purchaseButton().click() #Click on purchase button on checkout page 2

        assert "Success! Thank you!" in self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        print(checkoutPage.successMessage().text)

