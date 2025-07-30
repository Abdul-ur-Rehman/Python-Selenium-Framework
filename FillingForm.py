import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Jon Doe")
driver.find_element(By.NAME, "email").send_keys("jon@test.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("JONDOE123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male")
driver.find_element(By.ID, "inlineRadio2").click()
driver.find_element(By.NAME, "bday").send_keys("09-10-1998")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)


#For XPath --> //tagname[@attribute = 'value] --> //input[@type = 'submit']
#For CSS --> tagname[attribute = 'value] --> //input[@type = 'submit']
