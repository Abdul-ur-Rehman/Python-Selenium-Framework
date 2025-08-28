import pytest

from selenium import webdriver

from Project3_LightniesStudio_PSF.pageObjects.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption(
        "--bn", action="store", default="chrome"
    )
    parser.addoption(
        "--url", action="store", default="lightnines"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--bn")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        chromer_options = webdriver.ChromeOptions()
        chromer_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chromer_options)
    elif browser_name == "edge":
        service = webdriver.EdgeService(r"C:\Users\sg\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    if url == "lightnines":
        driver.get("https://lightnines.com")
    elif url == "TBA":
        driver.get("TBA")

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()

