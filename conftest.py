import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from Utilities.readProperties import READCONFIG
import pytest
from PageObjects.LoginPage import LoginPage



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

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def login(driver):
    BaseURL = READCONFIG.getapplicationurl()
    UserName = READCONFIG.getapplicationuserid()
    Password = READCONFIG.getapplicationpassword()
    driver.get(BaseURL)
    driver.implicitly_wait(5)
    driver.maximize_window()
    LP = LoginPage(driver)
    LP.setUserName(UserName)
    LP.setPassword(Password)
    LP.clickLogin()
    time.sleep(5)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )




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