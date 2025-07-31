import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
existed_list = ["Cauliflower - 1 Kg", "Carrot - 1 Kg", "Capsicum", "Cashews - 1 Kg"]
extracted_list = []
print(f"Existed List = {existed_list}")

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ca")
#wait = WebDriverWait(driver, 5)
#wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div/div/h4[@class='product-name']")))
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div/div/div/h4[@class='product-name']")

for product in products:
    extracted_list.append(product.text)

print(f"Extracted List = {extracted_list}")

assert extracted_list == existed_list

