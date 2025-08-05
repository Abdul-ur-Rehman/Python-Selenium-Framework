from selenium.webdriver.common.by import By

from Project1_ProtoCommerce_PSF.pageObjects.CheckoutPage import CheckoutPage


class ProductsPage:

    products_cards_loc = (By.XPATH, "//app-card-list/app-card/div")
    product_title_loc = (By.XPATH, "div/h4")
    product_cartButton_loc = (By.XPATH, "div/button")
    checkoutButton_loc = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def __init__(self, driver):
        self.driver = driver


    def productsCadsInfo(self):
        return  self.driver.find_elements(*ProductsPage.products_cards_loc)

    def extractProdcutTitle(self, product):
        return product.find_element(*ProductsPage.product_title_loc)

    def cartButton(self, product):
        return product.find_element(*ProductsPage.product_cartButton_loc)

    def checkoutButton(self):
        self.driver.find_element(*ProductsPage.checkoutButton_loc).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
