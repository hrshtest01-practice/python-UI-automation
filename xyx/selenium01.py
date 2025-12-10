import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(5)
time.sleep(10)
driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.XPATH,"//div[@class='autoSuggestPlugin hsw_autocomplePopup']/div/input").send_keys("delhi")
time.sleep(10)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
w= WebDriverWait(driver,10)
w.until(expected_conditions.visibility_of_element_located(By.ID,"ab")).click()

w= WebDriverWait(driver,10)
w.until(expected_conditions.element_to_be_clickable(By.XPATH,"")).click()
