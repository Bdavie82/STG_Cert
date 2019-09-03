from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class ErrorHandling:

    def clicklink(self, switch_driver, term):
        try:
            wait = WebDriverWait(switch_driver, 20)
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-uname=lotsearchLotmodel]")))
            switch_driver.find_elements(By.CSS_SELECTOR, "[data-uname=lotsearchLotmodel]")
        except NoSuchElementException:
            self.takescreenshot(switch_driver=switch_driver)
            print("Your search of " + term + " produced no results. Please refine your search term and try again")

        except TimeoutException:
            self.takescreenshot(switch_driver=switch_driver)
            print(
                "A timeout error has occured searching for " + term + ". Please refine your search term and try again")

    def takescreenshot(self, switch_driver):
        switch_driver.save_screenshot("test.png")
