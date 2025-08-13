from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing


#Add employee with mandatory fields	[Go to PIM > Add Employee > Fill mandatory fields > Save]	Employee added successfully

class PIM:
    PIM_link   = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    Add_Button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    Firstname_text ="//input[@placeholder='First Name']"
    Middlename_text ="//input[@placeholder='Middle Name']"
    Lastname_text = "//input[@placeholder='Last Name']"
    Save = "//button[@type='submit']"
    create_login_details="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    username='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    password='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    confirm_password ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'

    def __init__(self,driver):
        self.driver=driver

    def click_PIM_link(self):
        self.driver.find_element(By.XPATH,self.PIM_link).click()

    def click_Add_Button(self):
        self.driver.find_element(By.XPATH,self.Add_Button).click()

    def enter_Firstname_text(self,Fname):
        self.driver.find_element(By.XPATH,self.Firstname_text).send_keys(Fname)

    def enter_Middlename_text (self,Mname):
        self.driver.find_element(By.XPATH,self.Middlename_text).send_keys(Mname)

    def enter_Lastname_text(self,Lname):
        self.driver.find_element(By.XPATH,self.Lastname_text).send_keys(Lname)

    def click_Save_Emp(self):
        self.driver.find_element(By.XPATH,self.Save).click()

    def login_detail_slidbar(self):
        self.driver.find_element(By.XPATH,self.create_login_details).click()

    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    def enter_confirmpassword(self,cpassword):
        self.driver.find_element(By.XPATH,self.confirm_password).send_keys(cpassword)




