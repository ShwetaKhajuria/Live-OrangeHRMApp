from selenium.webdriver.common.by import By

#Add employee with mandatory fields	[Go to PIM > Add Employee > Fill mandatory fields > Save]	Employee added successfully

class PIM:
    PIM_link   = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    Add_Button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    Firstname_text ="//input[@placeholder='First Name']"
    Middlename_text ="//input[@placeholder='Middle Name']"
    Lastname_text = "//input[@placeholder='Last Name']"
    Save = "//button[@type='submit']"

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



