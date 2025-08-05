import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--bn", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver

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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
