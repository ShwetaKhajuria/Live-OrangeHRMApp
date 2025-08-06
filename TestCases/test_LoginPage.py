# TC001 Verify login with valid credentials (Admin / admin123)
# TC002 Verify login with invalid username
# TC003 Verify login with invalid password
# TC004 Verify login with empty username and password
# TC005 Check error message display for invalid login
import logging
import time
from logging import Logger
import pytest
from Utilities.customAssertions import assert_with_screenshot
from Utilities. customeLogger import LogGen
from Utilities.readProperties import READCONFIG
from conftest import driver
from PageObjects.LoginPage import LoginPage


BaseURL= READCONFIG.getapplicationurl()
UserName =READCONFIG.getapplicationuserid()
Password= READCONFIG.getapplicationpassword()

@pytest.mark.Sanity
def test_TC001_1_validcredentials(driver): # TC001 Verify login with valid credentials (Admin / admin123)
    logger = LogGen.loggen()

    logger.info("Test case -TC001 Verify login with valid credentials (Admin / admin123) [started] ")
    driver=driver
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
@pytest.mark.parametrize("username,password,expected_error,screenshot_name,test_description",
                        [
                            (UserName,"shweta","Invalid credentials","TC02_invalid.png","TC002: Invalid username"),
                            ("abcdes",Password,"Invalid credentials","TC03_invalid.png","TC003: Invalid Password"),
                            ("abcde","wrong","Invalid credentials","TC04_invalid.png","TC003: Invalid Username & Password"),
                            ("","","Required","TC05_invalid.png","TC005: Blank Password & Password")
                        ]

                        )
def test_TC001_2_Loginfailed(driver,username,password,expected_error,screenshot_name,test_description): # TC002 - TC005
    logger = LogGen.loggen()
    logger.info(f"{test_description} [Started]")
    driver=driver
    driver.get(BaseURL)
    driver.implicitly_wait(5)

    LP=LoginPage(driver)
    LP.setUserName(username)
    LP.setPassword(password)
    LP.clickLogin()
    time.sleep(5)

    logger.info(f"{test_description} [assertion started]")

    if expected_error in driver.page_source:
        assert True
    else:
        driver.save_screenshot(f"Screenshots/{screenshot_name}")
        assert False

    logger.info(f"{test_description} [Finished]")

