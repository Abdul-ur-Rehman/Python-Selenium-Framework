from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)

driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.XPATH, "//section/div/div/h2").text)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)