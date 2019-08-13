import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Flipkart (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get("https://www.flipkart.com/")

    def test01_hoverElectronics(self):
        self.driver.find_element_by_xpath("//button[@class = '_2AkmmA _29YdH8']").click()
        electronics = self.driver.find_element_by_xpath("//span[contains(text(),'Electronics')]")
        hover = ActionChains(self.driver).move_to_element(electronics)
        hover.perform()
        self.driver.implicitly_wait(10)

    def test02_selectProduct_srp(self):
        self.driver.find_element_by_xpath("//*[contains(text(),'Pixel 3a | 3a XL')]").click()

    def test_03_pdp(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'Google Pixel 3a (Just Black, 64 GB)')]").click()
        #go to the new window where the PDP opens
        self.driver.switch_to.window(self.driver.window_handles[1])
        title = self.driver.find_element_by_xpath("//span[@class='_35KyD6']")
        #check the product page title
        self.assertEqual(title.text, 'Google Pixel 3a (Just Black, 64 GB)  (4 GB RAM)')

    def test_04_addToCart(self):
        self.driver.find_element_by_xpath("//input[@id='pincodeInputId']").send_keys("560068")
        self.driver.find_element_by_xpath("//span[@class='_2aK_gu']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _2Npkh4 _2MWPVK']").click()

    def test_05_cartPage(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Cart')]").click()
        self.driver.implicitly_wait(10)
        plusbtn = self.driver.find_element_by_xpath("//button[text()='+']")
        self.driver.execute_script("arguments[0].click();", plusbtn)
        self.driver.implicitly_wait(15)
        self.driver.refresh()
        totalPayable = self.driver.find_element_by_xpath("//div[contains(text(),'Total Payable')]")
        print(totalPayable.text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()