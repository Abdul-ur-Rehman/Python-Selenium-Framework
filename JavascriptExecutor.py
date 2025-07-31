from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)

driver.execute_script("window.scrollBy(0,window.document.body.scrollHeight);")

driver.get_screenshot_as_file("test.png")