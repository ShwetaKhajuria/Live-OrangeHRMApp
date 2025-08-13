from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    header_dashboard_xpath = "//h6[normalize-space()='Dashboard']"
    button_profile_xpath ="//span[@class='oxd-userdropdown-tab']"
    button_logout_xpath ="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver =driver

    def Headerdisplayed(self):
        try:
                header = self.driver.find_element(By.XPATH, self.header_dashboard_xpath)
                return header.is_displayed()
        except:
                return False

    def Logout_displayed(self):
        try:
            self.driver.find_element(By.XPATH, self.button_profile_xpath).click()
            Logout_displayed = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH, self.button_logout_xpath))
            )
            return Logout_displayed.text
        except:
            return None

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.button_profile_xpath).click()
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()
