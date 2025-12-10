import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.ab-inbev.com/")


a1 = driver.find_element(By.ID,'country')
#time.sleep(5)
a2=Select(a1).select_by_visible_text("India")

driver.find_element(By.ID,"month").send_keys('11')
driver.find_element(By.ID,'day').send_keys('10')
driver.find_element(By.ID,"year").send_keys('2001')

b= WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable()

driver.find_element(By.XPATH,"//div/button[text()='Enter']").click()
#time.sleep(5)

