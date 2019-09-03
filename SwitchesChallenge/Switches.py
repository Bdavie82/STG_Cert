import unittest
import time

from SwitchesChallenge.DamageSwitcher import DamageSwitcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SwitchesChallenge.Setup import Setup


class SwitchesExercise(unittest.TestCase):

    def search(self, switch_driver):
        search_button = switch_driver.find_element_by_class_name("btn-lightblue")
        search_button.click()

    def searchTerm(self, term, switch_driver):
        search_input = switch_driver.find_element_by_id("input-search")
        search_input.send_keys(term)

    def navigateToPage(self, page, switch_driver):
        switch_driver.get(page)

    def changeEntries(self, switch_driver, entries):
        WebDriverWait(switch_driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,"
                                                                                     "\"inner-wrap\")]//div[contains("
                                                                                     "@class, ""\"top\")]//select[1]")))
        entries_field = switch_driver.find_element(By.XPATH,
                                                   "//div[contains(@class,\"inner-wrap\")]//div[contains(@class,"
                                                   "\"top\")]//select[1]").click()

        WebDriverWait(switch_driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,"
                                                                                     "\"inner-wrap\")]//div[contains("
                                                                                     "@class,""\"top\")]//select[1]"
                                                                                     "//option[3]"))).click()

        time.sleep(15)

    def countModels(self, switch_driver):

        wait = WebDriverWait(switch_driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-uname=lotsearchLotmodel]")))
        models = switch_driver.find_elements(By.CSS_SELECTOR, "[data-uname=lotsearchLotmodel]")

        all_models = []
        for m in models:
            all_models.append(m.get_attribute('innerHTML'))

        unique_models_dict = {}

        for x in all_models:
            if x not in unique_models_dict:
                unique_models_dict[x] = all_models.count(x)

        del unique_models_dict["[[ lm ]]"]

        for key, val in unique_models_dict.items():
            print(key, ":", val)

    def countDamages(self, switch_driver):
        wait = WebDriverWait(switch_driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-uname=lotsearchLotdamagedescription]")))
        damages = switch_driver.find_elements(By.CSS_SELECTOR, "[data-uname=lotsearchLotdamagedescription]")

        all_damages = []

        for m in damages:
            all_damages.append(m.get_attribute('innerHTML'))
            damage = m.get_attribute('innerHTML')
            print(DamageSwitcher().switchdamage(damage))

    def test_start(self):
        switch_driver = Setup().setup()
        self.navigateToPage("https://www.copart.com", switch_driver)
        self.searchTerm("porsche", switch_driver)
        self.search(switch_driver)
        self.changeEntries(switch_driver, 100)
        self.countModels(switch_driver)
        self.countDamages(switch_driver)

        switch_driver.implicitly_wait(10)


if __name__ == '__main__':
    unittest.main()
