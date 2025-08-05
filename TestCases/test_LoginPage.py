# TC001 Verify login with valid credentials (Admin / admin123)
# TC002 Verify login with invalid username
# TC003 Verify login with invalid password
# TC004 Verify login with empty username and password
# TC005 Check error message display for invalid login
import time

import pytest

from Utilities.customAssertions import assert_with_screenshot
from Utilities.customeLogger import LogGen
from Utilities.readProperties import READCONFIG
from conftest import setup
from PageObjects.LoginPage import LoginPage


BaseURL= READCONFIG.getapplicationurl()
UserName =READCONFIG.getapplicationuserid()
Password= READCONFIG.getapplicationpassword()

@pytest.mark.Sanity
def test_TC001_1_validcredentials(setup): # TC001 Verify login with valid credentials (Admin / admin123)
    logger=LogGen.loggen()
    logger.info("Test case -TC001 Verify login with valid credentials (Admin / admin123) [started] ")
    driver=setup
    driver.get(BaseURL)
    driver.implicitly_wait(5)

    LP=LoginPage(driver)
    LP.setUserName(UserName)
    #time.sleep(5)
    LP.setPassword(Password)
    LP.clickLogin()
    time.sleep(5)

    expected_title="OrangeHRM"
    actual_title=driver.title
    logger.info("Test case -TC001 Verify login with valid credentials (Admin / admin123)- [assertion]")
    assert_with_screenshot(driver=driver, actual=actual_title, expected=expected_title, message="Failed!!!!", screenshot_path="Screenshots/TC001.png")
    logger.info("Test case -TC001 Verify login with valid credentials (Admin / admin123) [Finished] ")

@pytest.mark.Regression
def test_TC001_2_Loginfailed(setup): # TC002 Verify login with invalid username
    logger=LogGen.loggen()
    logger.info("# TC002 Verify login with invalid username [Started]")
    driver=setup
    driver.get(BaseURL)
    driver.implicitly_wait(5)

    LP=LoginPage(driver)
    LP.setUserName("shweta")
    LP.setPassword(Password)
    LP.clickLogin()
    time.sleep(5)

    logger.info("Test case - TC002 Verify login with invalid username [assertion]")

    if "Invalid credentials" in driver.page_source:
        assert True
    else:
        driver.save_screenshot("/Screenshots/TC002.png")
        assert False

    logger.info("Test case- TC002 Verify login with invalid username [Completed] ")









