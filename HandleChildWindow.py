from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)


driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[1])

print(driver.find_element(By.TAG_NAME, "h3").text)

assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text