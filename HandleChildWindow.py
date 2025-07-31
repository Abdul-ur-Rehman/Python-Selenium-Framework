from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)


driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[1])
msg = driver.find_element(By.TAG_NAME, "h3").text
print(msg)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "New Window" == msg
