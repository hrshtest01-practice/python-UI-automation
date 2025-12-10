import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")

#driver.find_element(By.XPATH,'//div/input[@class="react-autosuggest_'_input react-autosuggest__input--open"]"]').send_keys("indore")
time.sleep(5)
driver.find_element(By.XPATH,'//li[@class="menu_Hotels"]/span/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//div/input[@placeholder="Where do you want to stay?"]').click()
time.sleep(5)


def ccr_flow(self):
    """This task runs repeatedly — each time gets a new CCR number and submits."""
    if not self.token:
        print("⚠️ Skipping, token not available.")
        return

    # Step 1: Get new CCR number
    headers = {
        "Authorization": f"Bearer {self.token}",
    }
    payload = {
        "HSCodes": "30021210"
    }

    response = self.client.get("/3c_ccr/api/ccr/GetCCRQNADocumentByHSCodes", headers=headers)
    try:
        data = response.json()
        self.ccr_no = data.get("CCRReferenceNo") or data.get("CCRNo")
        print(f"📄 CCR Number received: {self.ccr_no}")
    except Exception as e:
        print(f"❌ Failed to parse CCR number: {e}")
        return

    # Step 2: Submit CCR using the dynamic CCR number
    self.submit_ccr(headers)
