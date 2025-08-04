from selenium.webdriver.common.by import By

from PythonSeleniumFramework.pageObjects.ProductsPage import ProductsPage


class HomePage:

    shop = (By.XPATH, "//a[text()='Shop']")


    def __init__(self, driver):
        self.driver = driver


    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        productsPage = ProductsPage(self.driver)
        return productsPage