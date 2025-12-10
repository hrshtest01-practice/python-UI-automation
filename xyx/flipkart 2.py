import time
from os import times
import locust

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

driver.find_element(By.XPATH,'//div/input[@class="Pke_EE"]').send_keys("computer s")
time.sleep(3)

driver.find_element(By.XPATH,'//div/input[@class="Pke_EE"]').click()
time.sleep(5)
driver.find_element(By.XPATH,"//ul/li/div/a/div[text()='peakers']").click()
time.sleep(5)
driver.find_element(By.XPATH,'//div/div/div/a[@title="ZEBRONICS Zeb - Wonderbar 10 10 W Laptop/Desktop Speaker"]').click()
time.sleep(8)
driver.find_element(By.ID,'pincodeInputId').send_keys('452018')
time.sleep(7)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(5)