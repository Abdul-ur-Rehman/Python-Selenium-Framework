from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class HomePage():

    #Locators
    logo_loc = (By.CSS_SELECTOR, "img[alt='Logo']")
    nav_loc = (By.CSS_SELECTOR, "nav ul li a span[class='menu-item-text']")
    heroText_loc = (By.CSS_SELECTOR, "h1.elementor-headline")
    uploadLogoButton_loc = (By.XPATH, "//span[text()='Upload Your Logo']")
    createYourSign_loc = (By.XPATH, "//span[text()='Create Your Own Sign']")



    def __init__(self, driver):
        self.driver = driver

    def is_logo_displayed(self):
        return self.driver.find_element(*self.logo_loc).is_displayed()


    def get_navigation_links(self):
        return self.driver.find_elements(*self.nav_loc)

    def get_hero_section_text(self):
        return self.driver.find_element(*self.heroText_loc).text

    def upload_logo_Button(self):
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.uploadLogoButton_loc)
        )

    def create_Sign_Button(self):
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.createYourSign_loc)
        )


