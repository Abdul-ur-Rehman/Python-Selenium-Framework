import time
from PythonSeleniumFramework.pageObjects.HomePage import HomePage
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestHomePageFormFilling(BaseClass):

    def test_formFilling(self, setup):
        homePage = HomePage(self.driver)

        homePage.nameForm().send_keys("Jon Doe")
        homePage.emailForm().send_keys("jon@test.com")
        homePage.passwordForm().send_keys("JONDOE123")
        homePage.checkboxForm().click()
        self.selectOptionByText(homePage.genderForm(), "Male")
        homePage.radioButtonForm().click()
        homePage.dateForm().send_keys("09-10-1998")
        homePage.submitButtonForm().click()
        message = homePage.successMessageForm().text
        print(message)

        assert "Success" in message

time.sleep(2)
