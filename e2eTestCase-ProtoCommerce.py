from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)
#driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Shop']").click()
products = driver.find_elements(By.XPATH,"//app-card-list/app-card/div")

for product in products:
    if product.find_element(By.XPATH,"div/h4").text == "Blackberry":
        print(product.find_element(By.XPATH,"div/h4").text)
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CLASS_NAME,"btn-success").click()
driver.find_element(By.ID, "country").send_keys("pa")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Pakistan']")))

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Pakistan']")).click().perform()

driver.find_element(By.CSS_SELECTOR,".checkbox").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()

assert "Success! Thank you!" in driver.find_element(By.CSS_SELECTOR,".alert-success").text
print(driver.find_element(By.CSS_SELECTOR,".alert-success").text)

