import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
driver.maximize_window()
driver.get("https://www.amazon.in/")
searchBar = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
searchBar.send_keys("iPhone 7 32 gb(black)")
searchBar.send_keys(Keys.RETURN)
#select phone from SRP
driver.find_element_by_xpath("//span[contains(text(),'Apple iPhone 7 (32GB) - Black')]").click()
# go to the new window where the PDP opens
driver.switch_to.window(driver.window_handles[1])
amazonPrice = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
#print(amazonPrice)
driver.quit()

driver2 = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
driver2.maximize_window()
driver2.get("https://www.flipkart.com/")
driver2.find_element_by_xpath("//button[@class = '_2AkmmA _29YdH8']").click()
searchBar = driver2.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
searchBar.send_keys("iPhone 7 32 gb(black)")
searchBar.send_keys(Keys.RETURN)
driver2.implicitly_wait(15)
driver2.find_element_by_xpath("//div[contains(text(),'Apple iPhone 7 (Black, 32 GB)')]").click()
# go to the new window where the PDP opens
driver2.switch_to.window(driver2.window_handles[1])
flipkartPrice = driver2.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
print(flipkartPrice)
driver2.quit()

if amazonPrice == flipkartPrice :
    print("The prices are same!!")
elif amazonPrice > flipkartPrice :
    print("The price on Flipkart is lesser!!")
else:
    print("The price on Amazon is lesser!!")


