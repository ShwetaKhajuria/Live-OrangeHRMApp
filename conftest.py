import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.service import Service



@pytest.fixture()
def driver(browser):
    if browser.lower() == "chrome":
        service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")  # or pass executable_path
        driver = webdriver.Chrome(service=service)
    elif browser.lower() == "edge":
        service = Service(executable_path="C:/Drivers/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#************Pytest HTML Report *******************

def pytest_html_report_title(report):
    report.title = "Orange HRM Report Title"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append('<p><b>Project Name:</b> Orange HRM</p>')
    prefix.append('<p><b>Module Name:</b> My Info</p>')
    prefix.append('<p><b>Tester Name:</b> Shweta Khajuria</p>')

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Remove unwanted default keys if you want
    metadata.pop("Plugins", None)