'''
Add employee with mandatory fields	Go to PIM > Add Employee > Fill mandatory fields > Save	Employee added successfully
Add employee with login details	> Enable “Create Login Details” > Fill > Save	Login created for employee
Add employee with empty name	Leave name fields blank → Click Save	Error: "Required" displayed
Search for existing employee	Enter valid name > Click Search	Employee appears in results
Search with invalid name	Enter invalid name > Click Search	"No records found" displayed
'''
import time
from PageObjects.PIM import PIM

def test_TC008_SaveEmployee(driver,login):
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





