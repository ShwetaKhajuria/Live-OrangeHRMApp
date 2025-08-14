'''
TC09 - Add employee with mandatory fields	Go to PIM > Add Employee > Fill mandatory fields > Save	Employee added successfully
TC10 - Add employee with login details	> Enable “Create Login Details” > Fill > Save	Login created for employee
TC11 - Add employee with empty name	Leave name fields blank → Click Save	Error: "Required" displayed
TC12 - Search for existing employee	Enter valid name > Click Search	Employee appears in results
TC13 - Search with invalid name	Enter invalid name > Click Search	"No records found" displayed
'''
import time

from openpyxl.utils import rows_from_range
from selenium.webdriver.common.by import By

from PageObjects.PIM import PIM

# TC09 - Add employee with mandatory fields	Go to PIM > Add Employee > Fill mandatory fields > Save	Employee added successfully
def test_TC009_SaveEmployee(driver,login):
    driver.implicitly_wait(5)
    PIM_Ob =PIM(driver)
    PIM_Ob.click_PIM_link()
    PIM_Ob.click_Add_Button()
    PIM_Ob.enter_Firstname_text("Henry")
    PIM_Ob.enter_Middlename_text("K")
    PIM_Ob.enter_Lastname_text("Smittens")
    time.sleep(5)
    PIM_Ob.click_Save_Emp()
    time.sleep(5)

    if "Henry" and "Smittens" in driver.page_source:
        assert True
    else:
        assert False

# TC10 - Add employee with login details	> Enable “Create Login Details” > Fill > Save	Login created for employee
def test_TC010_logincreation(driver,login):
    driver.implicitly_wait(5)
    PIM_Ob = PIM(driver)
    PIM_Ob.click_PIM_link()
    PIM_Ob.click_Add_Button()
    PIM_Ob.enter_Firstname_text("Henry")
    PIM_Ob.enter_Middlename_text("K")
    PIM_Ob.enter_Lastname_text("Smittens")
    PIM_Ob.login_detail_slidbar()
    PIM_Ob.enter_username("HenrykSmittens2")
    PIM_Ob.enter_password("admin123")
    PIM_Ob.enter_confirmpassword("admin123")
    PIM_Ob.click_Save_Emp()

    if "Henry" and "Smittens" in driver.page_source:
        assert True
    else:
        assert False


#TC11 - Add employee with empty name	Leave name fields blank → Click Save	Error: "Required" displayed
def test_TC011_nousername(driver,login):
    driver.implicitly_wait(5)
    PIM_Ob = PIM(driver)
    PIM_Ob.click_PIM_link()
    PIM_Ob.click_Add_Button()
    PIM_Ob.enter_Firstname_text("")
    PIM_Ob.enter_Middlename_text("K")
    PIM_Ob.enter_Lastname_text("Smittens")
    PIM_Ob.click_Save_Emp()
    time.sleep(5)
    if "Required" in driver.page_source:
        assert True
    else:
        assert False


#TC12 - Search for existing employee	Enter valid name > Click Search	Employee appears in results
def test_TC012_SearchUser(driver,login):
    PIM_Ob = PIM(driver)
    driver.maximize_window()
    PIM_Ob.click_PIM_link()
    PIM_Ob.enter_Employee_name("Charles")
    PIM_Ob.click_search()
    time.sleep(5)
    name_found = False
    rows = driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]')
    for row in rows:
        if row.text=="Charles":
            name_found=True
            assert True
            break
        else:
            assert False











