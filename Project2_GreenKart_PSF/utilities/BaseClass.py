import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        if not logger.handlers:
            filehandler = logging.FileHandler(
                r"D:\QA Automation\Selenium-Python\Project2_GreenKart_PSF\utilities\logfile.log")
            formatting = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
            filehandler.setFormatter(formatting)
            logger.addHandler(filehandler)  # filehandler object
            logger.setLevel(logging.INFO)

        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{text}']")))

    def selectCountry(self, locator, country):
        select = Select(locator)
        select.select_by_visible_text(country)