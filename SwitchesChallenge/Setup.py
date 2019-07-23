import unittest
from selenium import webdriver


class Setup(unittest.TestCase):

    def setup(self):
        # code to startup webdriver
        # BDAVIE 4-15-2019
        # Since I run on a MAC I have to remove the .exe for things to run properly
        self.driver = webdriver.Chrome("../chromedriver")
        return self.driver

    def teardown(self):
        # code to close webdriver.
        self.driver.close()

    # def test_driver(self):
    #     self.setup()
    #     self.driver.get("https://www.google.com")


if __name__ == '__main__':
    unittest.main()
