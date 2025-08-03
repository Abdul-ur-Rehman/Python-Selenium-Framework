from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)
elements_list = []
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
elements = driver.find_elements(By.XPATH, "//tr/td[1]")

for element in elements:
    elements_list.append(element.text)

elements_sorted = elements_list.copy()

assert elements_sorted == elements_list