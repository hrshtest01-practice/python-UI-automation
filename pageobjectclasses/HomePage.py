from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    name = (By.XPATH, '//div/input[@name="name"]')
    pswd = (By.CSS_SELECTOR, "[id='exampleInputPassword1']")
    email = (By.CSS_SELECTOR,"[name ='email']")
    gender = (By.ID,"exampleFormControlSelect1")
    status =(By.ID,"inlineRadio1")
    submit = (By.CSS_SELECTOR,"[type='submit']")
    assertionmsg = (By.CLASS_NAME,"alert-success")
    name2= (By.XPATH,"//h4/input")

    def __init__(self, driver):
        self.driver = driver

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def gatemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword (self):
        return self.driver.find_element(*HomePage.pswd)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def selectstatus(self):
        return self.driver.find_element(*HomePage.status)

    def getsubmitbtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getalertmsg(self):
        return self.driver.find_element(*HomePage.assertionmsg)

    def getnameagain(self):
        return self.driver.find_element(*HomePage.name2)
