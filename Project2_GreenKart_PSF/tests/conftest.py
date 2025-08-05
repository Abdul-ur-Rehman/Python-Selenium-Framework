import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver = driver
    yield
    driver.quit()