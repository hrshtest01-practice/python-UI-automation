import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from xyx.programs import driver


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectoptions(self, selectelement, text):
        sel = Select(selectelement)
        sel.select_by_visible_text(text)

    def explicitwait(self,element):
        #WebDriverWait(self.driver,5).until(expected_conditions.presence_of_element_located(element))
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(element))