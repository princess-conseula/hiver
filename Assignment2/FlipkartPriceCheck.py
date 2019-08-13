import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Flipkart (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get("https://www.flipkart.com/")

    def test_01_search(self):
        self.driver.find_element_by_xpath("//button[@class = '_2AkmmA _29YdH8']").click()
        searchBar = self.driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
        searchBar.send_keys("iPhone 7 32 gb(black)")
        searchBar.send_keys(Keys.RETURN)

    def test_02_getPrice(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone 7 (Black, 32 GB)')]").click()
        # go to the new window where the PDP opens
        self.driver.switch_to.window(self.driver.window_handles[1])
        flipkartPrice = self.driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
        print(flipkartPrice)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()