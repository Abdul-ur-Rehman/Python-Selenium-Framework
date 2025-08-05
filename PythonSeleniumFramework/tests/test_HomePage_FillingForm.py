import pytest
from PythonSeleniumFramework.pageObjects.HomePage import HomePage
from PythonSeleniumFramework.testData.HomePageTestData import HomePageTestData
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestHomePageFormFilling(BaseClass):

    def test_formFilling(self, setup, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        homePage.nameForm().send_keys(getData["firstname"])
        log.info("Entering firstname")
        homePage.emailForm().send_keys(getData["email"])
        log.info("Entering email")
        homePage.passwordForm().send_keys(getData["password"])
        log.info("Entering password")
        homePage.checkboxForm().click()
        log.info("Clicking checkbox")
        self.selectOptionByText(homePage.genderForm(), getData["gender"])
        log.info("Selecting gender as Male")
        homePage.radioButtonForm().click()
        log.info("Clicking radio button")
        homePage.dateForm().send_keys(getData["date"])
        log.info("Selecing date")
        homePage.submitButtonForm().click()
        log.info("Clicking submit button")
        message = homePage.successMessageForm().text
        print(message)

        assert "Success" in message
        self.driver.refresh()
        log.info("Refreshing Page")

    @pytest.fixture(params= HomePageTestData.data)
    def getData(self, request):
        return request.param



