from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Array:

    def makesmodels(self, switch_driver):
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

        makemodellinks = switch_driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/fragment[3]/div[1]/div["
                                                               "1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div["
                                                               "1]/div[2]/div[*]/ul[1]/li[*]/a[1]")

        allmodelsandlinks = []
        for m in makemodellinks:
            alllinks = []
            alllinks.append(m.get_attribute('href'))
            alllinks.append(m.get_attribute('innerHTML'))  # m.get_attribute('href') or m.get_attribute('innerHTML')
            allmodelsandlinks.append(alllinks)

        return makemodellinks
