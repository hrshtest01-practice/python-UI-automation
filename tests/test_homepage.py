import time

from selenium.webdriver.support.wait import WebDriverWait

from pageobjectclasses.HomePage import HomePage
# from tests.contest import driver, setup
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):
    # @pytest.mark.order(2)
    def test_name(self):
        home = HomePage(self.driver)
        home.getname().send_keys("harsh")
        time.sleep(3)
        print("harsh bhawsar")

    def test_email(self):
        home = HomePage(self.driver)
        home.gatemail().send_keys("harsh@yopmail.com")
        time.sleep(2)

    # @pytest.mark.order(3)
    def test_password(self):
        home = HomePage(self.driver)
        home.getpassword().send_keys("Harsh@123")
        time.sleep(4)

    # @pytest.mark.order(4)
    def test_options(self):
        home = HomePage(self.driver)
        self.selectoptions(home.getgender(), "Female")

    def test_status(self):
        home = HomePage(self.driver)
        home.selectstatus().click()

    def test_submitbtn(self):
        home = HomePage(self.driver)
        home.getsubmitbtn().click()

    def test_assertmsg(self):
        home = HomePage(self.driver)
        time.sleep(3)
        asserttext = home.getalertmsg().text
        assert "successfully" in asserttext
        print('its working')

    def test_name2(self):
        home=HomePage(self.driver)
        self.explicitwait(home.name2)
        home.getnameagain().send_keys('harsh')
        time.sleep(5)


