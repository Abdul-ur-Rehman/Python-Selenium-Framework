from selenium.webdriver.common.by import By


class HomePage:

    searchBar_loc = (By.CLASS_NAME, "search-keyword")
    productCards_loc = (By.XPATH, "//div/div[@class='product']")


    def searchBar_HomePage(self):
        return self.driver.find_element(*HomePage.searchBar_loc)

    def productCards_HomePage(self):
        return self.driver.find_element(*HomePage.productCards_loc)