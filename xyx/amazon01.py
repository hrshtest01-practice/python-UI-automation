import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(7)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('iPhone')
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
time.sleep(5)
all=driver.find_elements(By.XPATH,"//a/h2/span[contains(text(),'iPhone')]")
time.sleep(5)
print(len(all),all)
time.sleep(5)
driver.find_element(By.XPATH,"//a/span/span/span[text()='51,499']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//ul[1]/li/span/span[@id='color_name_1'][1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@title='Add to Shopping Cart']").click()
time.sleep(7)