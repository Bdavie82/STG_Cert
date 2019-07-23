import unittest
import time
from typing import List, Any

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SwitchesChallenge.Setup import Setup


# all_damages: List[Any] = []

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

        # all_models = [m.get_attribute('innerHTML') for m in models]

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

        # Started doing it this way then realized that a dictionary with a key,value pair was the way to go.
        # unique_models = []
        # models_count = []
        # for x in all_models:
        #     if x not in unique_models:
        #         unique_models.append(x)
        #     models_count.append(all_models.count(x))
        #
        # # print(unique_models)
        # for m in unique_models:
        #     print(m + str(models_count)[1:-1])

        switch_driver.implicitly_wait(10)

    def countDamages(self, switch_driver):
        wait = WebDriverWait(switch_driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-uname=lotsearchLotdamagedescription]")))
        damages = switch_driver.find_elements(By.CSS_SELECTOR, "[data-uname=lotsearchLotdamagedescription]")

        all_damages = []

        for m in damages:
            all_damages.append(m.get_attribute('innerHTML'))

        unique_damage = {}
        #
        # for d in all_damages:
        #     self.switchdamage(d, all_damages)

        switch_driver.implicitly_wait(10)

    def test_start(self):
        switch_driver = Setup().setup()
        self.navigateToPage("https://www.copart.com", switch_driver)
        self.searchTerm("porsche", switch_driver)
        self.search(switch_driver)
        self.changeEntries(switch_driver, 100)
        self.countModels(switch_driver)
        self.countDamages(switch_driver)

        switch_driver.implicitly_wait(10)


class DamageSwitcher(object):
    def damage_type_to_count(self, damage_idx):
        damage_count = 'damage_' + str(damage_idx)
        method = getattr(self, damage_count, lambda: "MISC")
        return method()

    def damage_1(self):
        return "REAR_END"

    def damage_2(self):
        return "FRONT END"

    def damage_3(self):
        return "MINOR DENT/SCRATCHES"

    def damage_4(self):
        return "UNDERCARRIAGE"

    # def switchdamage(self, damage):
    #     damage_type = {
    #         "REAR END": 0,
    #         "FRONT END": 0,
    #         "MINOR DENT/SCRATCHES": 0,
    #         "UNDERCARRIAGE": 0,
    #         "MISC": 0
    #     }
    #
    #     # damage_type[damage] = all_damages.count(damage)
    #
    #     func = damage_type.get(damage, lambda: "MISC")
    #     # print(damage_type.get(damage, "MISC"))
    #
    #     return func()
        time.sleep(15)


if __name__ == '__main__':
    unittest.main()
