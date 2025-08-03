from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radios = driver.find_elements(By.XPATH, " //input[@type='radio']")

print(len(radios))

for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()

        break