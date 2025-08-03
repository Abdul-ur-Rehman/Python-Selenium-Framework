from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e_ProtoCommerce(self, setup):
        self.driver.implicitly_wait(4)


        self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        products = self.driver.find_elements(By.XPATH, "//app-card-list/app-card/div")

        for product in products:
            if product.find_element(By.XPATH, "div/h4").text == "Blackberry":
                print(product.find_element(By.XPATH, "div/h4").text)
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        self.driver.find_element(By.ID, "country").send_keys("pa")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Pakistan']")))

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[text()='Pakistan']")).click().perform()

        self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

        assert "Success! Thank you!" in self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        print(self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text)

