from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Test_GreenKart:

    existed_list = ["Cauliflower - 1 Kg", "Carrot - 1 Kg", "Capsicum", "Cashews - 1 Kg"]
    extracted_list = []

    def test_e2e_GreenKart(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.implicitly_wait(4)


        driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ca")
        products = driver.find_elements(By.XPATH, "//div/div[@class='product']")

        assert len(products) > 0
        #Extract product titles
        for product in products:
            self.extracted_list.append(product.find_element(By.XPATH,"h4[@class='product-name']").text)
            product.find_element(By.XPATH, "div[@class='product-action']").click()

        #Validation that extracted and existed lists are same
        assert self.existed_list == self.extracted_list

        driver.find_element(By.CLASS_NAME, "cart-icon").click()
        driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

        #Validation that Sum of all products in the table is same as the total of all the products shown
        actual_Total = 0
        prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

        for price in prices:
            actual_Total = actual_Total + int(price.text)

        total_Amount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

        assert actual_Total == total_Amount

        driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
        driver.find_element(By.CLASS_NAME, "promoBtn").click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

        #Validation that discount price is less than the total amount

        discount_Amt = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

        assert discount_Amt < total_Amount

        driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

        select = Select(driver.find_element(By.XPATH, "//select"))
        select.select_by_visible_text("Pakistan")

        driver.find_element(By.CLASS_NAME, "chkAgree").click()
        driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

        driver.quit()










