import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
time.sleep(3)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("phone")
time.sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(3)
a= driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result'][1]//span[@class='a-price-whole']").text
#driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result'][1]//img").click()
print(a)
time.sleep(3)
driver.find_element(By.XPATH,"//ul/span/span//a/span[text()='Samsung']/../../a").click()
time.sleep(5)
