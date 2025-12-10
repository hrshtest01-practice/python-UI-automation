import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.XPATH,"//div[@id='content']/div/a").click()
time.sleep(2)
print((driver.current_window_handle).title())
a=driver.window_handles
driver.switch_to.window(a[0])
print(a)
print(driver.title)
time.sleep(5)
