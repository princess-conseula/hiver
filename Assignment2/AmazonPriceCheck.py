import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Amazon (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.in/")

    def test_01_search(self):
        searchBar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        searchBar.send_keys("iPhone 7 32 gb(black)")
        searchBar.send_keys(Keys.RETURN)

    def test_02_getPrice(self):
        #select phone from SRP
        self.driver.find_element_by_xpath("//span[contains(text(),'Apple iPhone 7 (32GB) - Black')]").click()
        # go to the new window where the PDP opens
        self.driver.switch_to.window(self.driver.window_handles[1])
        amazonPrice = self.driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
        print(amazonPrice)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
