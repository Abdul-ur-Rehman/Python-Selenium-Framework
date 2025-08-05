import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--bn", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--bn")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "edge":
        obj = Service(r"C:\Users\sg\Downloads\edgedriver_win64\msedgedriver.exe""")
        driver = webdriver.Edge(service=obj)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()