'''
TC08 - Add employee with mandatory fields	Go to PIM > Add Employee > Fill mandatory fields > Save	Employee added successfully
TC09 - Add employee with login details	> Enable “Create Login Details” > Fill > Save	Login created for employee
TC10 - Add employee with empty name	Leave name fields blank → Click Save	Error: "Required" displayed
TC11 - Search for existing employee	Enter valid name > Click Search	Employee appears in results
TC12 - Search with invalid name	Enter invalid name > Click Search	"No records found" displayed
'''
import time
from PageObjects.PIM import PIM

# TC08 - Add employee with mandatory fields	Go to PIM > Add Employee > Fill mandatory fields > Save	Employee added successfully
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

# TC09 - Add employee with login details	> Enable “Create Login Details” > Fill > Save	Login created for employee
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
    time.sleep(5)

    if "Henry" and "Smittens" in driver.page_source:
        assert True
    else:
        assert False







