'''
TC005	Verify user lands on Dashboard after login	Login as Admin	Dashboard header should be visible
TC006	Verify user profile dropdown	Click on profile icon (top right)	Logout option should appear
TC007	Verify logout	Click profile icon > Click Logout	User is redirected to login page
'''


import time
from PageObjects.DashboardPage import DashboardPage
from Utilities.customAssertions import assert_with_screenshot
from conftest import driver


def test_TC005_Dashboardheader(driver,login):    #TC005	 Verify user lands on Dashboard after login
   driver=login
   driver.implicitly_wait(5)
   DP=DashboardPage(driver)
   time.sleep(5)
   if DP.Headerdisplayed():
       assert True
   else:
       driver.save_screenshot("Screenshots/TC002_1.png")
       assert False

def test_TC006_CheckLogout(driver,login): # TC006 Logout option should appear
    driver=login
    driver.implicitly_wait(5)
    dashboard = DashboardPage(driver)
    logout_text = dashboard.Logout_displayed()
    #print(f"Logout text returned: '{logout_text}'")
    assert logout_text == "Logout", "Logout option not displayed correctly"


def test_TC007_Logout (driver,login):    # TC007  User is redirected to login page
    driver=login
    driver.implicitly_wait(5)
    LO=DashboardPage(driver)
    LO.clickLogout()
    expected_title="OrangeHRM"
    assert_with_screenshot(driver, actual=driver.title, expected=expected_title, message="Logout_Successful", screenshot_path="Screenshots/TC006.png")