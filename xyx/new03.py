import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(25)
driver.get("https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Fully%20Automatic%20Front%20Load")
driver.find_element(By.XPATH,"//div[@title='Samsung']").click()
time.sleep(6)

from selenium import webdriver

driver = webdriver.Chrome()
