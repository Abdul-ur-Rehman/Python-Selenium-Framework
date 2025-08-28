
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions as EC


class UploadLogoPage:

    #Locators
    fullName_loc = (By.ID, "wpforms-13512-field_1")
    email_loc = (By.ID, "wpforms-13512-field_2")
    country_loc = (By.CLASS_NAME, "iti__country-container")
    flag_loc = (By.XPATH, "//span[text()='Pakistan']")
    phone_loc = (By.ID, "wpforms-13512-field_3")
    budgetDropdown_loc = (By.CSS_SELECTOR, ".choices__list.choices__list--single")
    budgetIdeaText_loc = (By.XPATH, "//div/div[text()='$650 - $1000']")
    signTypes_loc = (By.ID, "wpforms-13512-field_10")
    uploadFile_loc = (By.ID, "wpforms-13512-field_6")
    textarea_loc = (By.XPATH, "//textarea[@id='wpforms-13512-field_7']")
    submitButton_loc = (By.CSS_SELECTOR, "button[type='submit']")
    successMessage_loc = (By.ID, "wpforms-confirmation-13512")

    def __init__(self, driver):
        self.driver = driver

    def enter_fullName(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.fullName_loc)).send_keys(name)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_loc)).send_keys(email)

    def countryFlag(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.country_loc)).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.flag_loc)).click()

    def enter_phone(self, phone):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.phone_loc)).send_keys(phone)

    def select_budget(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.budgetDropdown_loc)).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.budgetIdeaText_loc)).click()

    def select_SignTypes(self):
        allSigns = self.driver.find_elements(*self.signTypes_loc)

        for sign in allSigns:
            sign.click()


    def uploadFile(self):
        # Wait for the dropzone element
        dropzone = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".wpforms-uploader.dz-clickable"))
        )

        # Click the dropzone to create the hidden input
        self.driver.execute_script("arguments[0].click();", dropzone)

        # Now wait for the hidden input[type='file'] to appear inside the dropzone
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".wpforms-uploader input[type='file']"))
        )

        # Make it visible (optional)
        self.driver.execute_script("arguments[0].style.display='block';", file_input)

        # Send file path
        file_input.send_keys(r"C:\Users\sg\Downloads\gazelle-indoor-shoes.png")

        #WebDriverWait(self.driver, 10).until(
        #    EC.presence_of_element_located(self.uploadFile_loc)).send_keys(r"C:\Users\sg\Downloads\gazelle-indoor-shoes.png")

    def textarea(self, text):
        return self.driver.find_element(*self.textarea_loc).send_keys(text)

    def click_submitButton(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.submitButton_loc)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_button)

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submitButton_loc)
        )

        try:
            submit_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", submit_button)

    def successMessageText(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.successMessage_loc))

        return self.driver.find_element(*self.successMessage_loc).text




