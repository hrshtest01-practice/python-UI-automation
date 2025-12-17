import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
time.sleep(8)
"""
a=driver.find_element(By.XPATH, "//div[@class='QSCKDh eRsYMo']/div[2]/div[not(.//div[contains(@class,'t7gRps')])]//div[@class='RG5Slk']").text
print(a)
time.sleep(7)"""

a=driver.find_element(By.XPATH,"//div[@class='QSCKDh eRsYMo']/div[2]/div//div[contains(text(),'POCO')]/../../div[@class='col col-5-12 mao5dl']//div[@class='hZ3P6w DeU9vF']").text
print(a)
time.sleep(5)