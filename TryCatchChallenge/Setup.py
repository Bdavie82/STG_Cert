import unittest
from selenium import webdriver
from selenium.webdriver.common import service


class Setup(unittest.TestCase):

    def setup(self):
        # code to startup webdriver
        # BDAVIE 4-15-2019
        # Updated 8-2-2019 to use service object rather than just webdriver
        self.driver = webdriver.Chrome("chromedriver")

        return self.driver

    def teardown(self):
        # code to close webdriver.
        self.driver.close()

    # def test_driver(self):
    #     self.setup()
    #     self.driver.get("https://www.google.com")


if __name__ == '__main__':
    unittest.main()
