from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class Array:

    def MakesModels(self, switch_driver):
        wait = WebDriverWait(switch_driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//body[@id='mainBody']/div[contains(@class,"
                                                               "'inner-wrap')]/div/fragment[@id='Serverside "
                                                               "Quickpicks']/div[contains(@class,'homepage "
                                                               "padLR')]/div[contains(@class,'container-fluid')]/div["
                                                               "contains(@class,'homepagecontent')]/div/div[contains("
                                                               "@class,'topspacing ct-container')]/div["
                                                               "@class='col-lg-9 col-md-8 col-xs-12']/div["
                                                               "@class='tab-content']/div[@id='tabTrending']/div["
                                                               "1]/div[2]")))

        models = switch_driver.find_elements(By.XPATH, "//body[@id='mainBody']/div[contains(@class,"
                                                       "'inner-wrap')]/div/fragment[@id='Serverside "
                                                       "Quickpicks']/div[contains(@class,'homepage "
                                                       "padLR')]/div[contains(@class,'container-fluid')]/div["
                                                       "contains(@class,'homepagecontent')]/div/div[contains("
                                                       "@class,'topspacing ct-container')]/div["
                                                       "@class='col-lg-9 col-md-8 col-xs-12']/div["
                                                       "@class='tab-content']/div[@id='tabTrending']/div["
                                                       "1]/div[2]")
        switch_driver.implicitly_wait(10)
        alllinks_dict = {}

        # for m in models

        return models
