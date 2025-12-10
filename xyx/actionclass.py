import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver= webdriver.Chrome()
driver.get("file:///C:/Users/harsh.bhawsar_infobe/Desktop/dropdown.html")
time.sleep(3)
dropdown=driver.find_element(By.ID,"cars")

#click
actions=ActionChains(driver)
actions.move_to_element(dropdown).perform()
time.sleep(2)
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//div/ul/a[@title='Orders']"))).click()
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
actions.send_keys(Keys.ENTER).perform()
time.sleep(2)
