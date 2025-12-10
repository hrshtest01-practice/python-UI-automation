import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login.php/")
driver.find_element(By.ID,"email").send_keys("harshbhawar@gmail.com")
driver.find_element(By.ID,"pass").send_keys("12345676")
time.sleep(5)
a= driver.window_handles
print(a,len(a))
time.sleep(5)
driver.switch_to.window(a[2])
time.sleep(5)

