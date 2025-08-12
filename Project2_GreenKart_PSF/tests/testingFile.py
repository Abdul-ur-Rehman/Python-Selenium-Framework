import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chromer_options = webdriver.ChromeOptions()
chromer_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chromer_options)
driver.implicitly_wait(5)
driver.get("https://lightnines.com")


action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "span[class ='tools-icon header-search-icon']")).click().perform()
#action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


#driver.find_element(By.CSS_SELECTOR, "span[class ='tools-icon header-search-icon']").click()
time.sleep(4)
driver.find_element(By.CLASS_NAME, "search-field").is_displayed()
#time.sleep(4)