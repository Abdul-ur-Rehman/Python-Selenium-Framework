from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.switch_to.window(driver.window_handles[1])
sentence = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text
print(sentence)
email = [word for word in sentence.split() if "@" in word and "." in word][0]
print(email)

driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.NAME, "username").send_keys(email)
driver.find_element(By.NAME, "signin").click()

error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text

print(error_msg)