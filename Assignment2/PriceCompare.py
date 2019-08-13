import unittest
import AmazonPriceCheck
import FlipkartPriceCheck


# get all tests from SearchText and HomePageTest class
amazon = unittest.TestLoader().loadTestsFromTestCase(AmazonPriceCheck.Amazon)
flipkart = unittest.TestLoader().loadTestsFromTestCase(FlipkartPriceCheck.Flipkart)

# create a test suite combining search_text and home_page_test
test_suite_amazon = unittest.TestSuite([amazon])

amazonPrice = unittest.TextTestRunner(verbosity=3).run(test_suite_amazon)

test_suite_flipkart = unittest.TestSuite([flipkart])

flipkartPrice = unittest.TextTestRunner(verbosity=3).run(test_suite_flipkart)







