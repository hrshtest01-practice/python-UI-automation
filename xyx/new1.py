import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(5)

serch = driver.find_element(By.XPATH,'//div/input[@class="Pke_EE"]').send_keys("computer")
time.sleep(5)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(5)
driver.find_element(By.XPATH,'//span[text()="Electronics"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//div/div/a[@title="Mi"]').click()
time.sleep(5)


