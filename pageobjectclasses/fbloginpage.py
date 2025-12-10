from pluggy import HookImpl
from selenium.webdriver.common.by import By
from pageobjectclasses.HomePage import HomePage

class fbpage:

    name = (By.ID,"email")
    pswd = (By.ID,"pass")
    loginbtn = (By.ID,"loginbutton")

    def __init__(self, driver):
        self.driver = driver

    def getname(self):
        return self.driver.find_element(self.name)

    def getpassword(self):
        return self.driver.find_element(*fbpage.pswd)

    def loginbutton(self):
        return self.driver.find_element(*fbpage.loginbtn)


