import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from hamcrest import *
from pop_selenium.pages.home_page import HomePage
from pop_selenium.pages.search_page import SearchPage
from pop_selenium.pages.summary_page import SummaryPage


class TestAddToBasket(unittest.TestCase):

    def setUp(self):
        option = webdriver.FirefoxOptions()
        # option.add_argument("--headless")
        self.driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.summary_page = SummaryPage(self.driver)

    def test_add_to_basket(self):
        self.home_page.search_item("Printed Summer")
        self.search_page.add_to_basket()

        total_price = self.summary_page.get_total_price()
        shipping_price = self.summary_page.get_shipping_price()

        assert_that(total_price, less_than_or_equal_to(30))
        assert_that(shipping_price, equal_to(2))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
