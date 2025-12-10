import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/tables")
driver.find_element(By.XPATH,"//table[@id='table1']/thead/tr/th/span[text()='Due']").send_keys("is it mobile cover")
list1=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td[4]")
list2=[]
for i in range(len(list1)):
    a=list1[i].text
    list2.append(float(a[1::]))
new = list2
new.sort()
if list2 == new:
    print("its same")
else:
    print("its not working")

