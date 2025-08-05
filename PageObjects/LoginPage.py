from selenium.webdriver.common.by import By


class LoginPage:
    text_UserName_Xpath="//input[@placeholder='Username']"
    text_password_Xpath="//input[@placeholder='Password']"
    button_Login_Xpath="//button[@type='submit']"
    link_logout_Xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver =driver

    def setUserName(self,UserName):
        self.driver.find_element(By.XPATH,self.text_UserName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_UserName_Xpath).send_keys(UserName)

    def setPassword(self,Password):
        self.driver.find_element(By.XPATH,self.text_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_Xpath).send_keys(Password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_Login_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH,self.link_logout_Xpath).click()
