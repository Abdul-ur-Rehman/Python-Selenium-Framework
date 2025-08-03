import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ca")
time.sleep(2)

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

assert len(products) > 0

for product in products:
    product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()


#Validation of total sum with actual sum

prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
actualSum = 0
for price in prices:
    actualSum += int(price.text)
print(actualSum)

totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert actualSum == totalAmount


driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promo_text = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promo_text)

assert "Code applied ..!" in promo_text