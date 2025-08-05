from selenium.webdriver.common.by import By

from Project2_GreenKart_PSF.pageObjects.DiscountPage import DiscountPage


class HomePage:

    searchBar_loc = (By.CLASS_NAME, "search-keyword")
    productCards_loc = (By.XPATH, "//div/div[@class='product']")
    productTitle_loc = (By.XPATH, "h4[@class='product-name']")
    productCartButton_loc = (By.XPATH, "div[@class='product-action']")
    cartButtonHeader_loc = (By.CLASS_NAME, "cart-icon")
    checkoutButtonHeader_loc = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")



    def __init__(self, driver):
        self.driver = driver

    def searchBar_HomePage(self):
        return self.driver.find_element(*HomePage.searchBar_loc)

    def productCards_HomePage(self):
        return self.driver.find_elements(*HomePage.productCards_loc)

    def productTitle_HomePage(self, product):
        return product.find_element(*HomePage.productTitle_loc)

    def productCartButton_HomePage(self, product):
        return product.find_element(*HomePage.productCartButton_loc)

    def cartButtonHeader_HomePage(self):
        return self.driver.find_element(*HomePage.cartButtonHeader_loc)

    def checkoutButtonHeader_HomePage(self):
        self.driver.find_element(*HomePage.checkoutButtonHeader_loc).click()
        discountPage = DiscountPage(self.driver)
        return discountPage
