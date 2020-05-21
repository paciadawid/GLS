import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hamcrest import *
from pop_selenium.pages.home_page import HomePage


class TestAddToBasket(unittest.TestCase):

    def setUp(self):
        option = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.home_page = HomePage(self.driver)

    def test_add_to_basket(self):

        self.home_page.search_item("Printed Summer")

        product = self.driver.find_element_by_class_name("product-container")
        hover = ActionChains(self.driver).move_to_element(product)
        hover.perform()
        self.driver.find_element_by_xpath("//*[@title='Add to cart']").click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@title='Proceed to checkout']"))).click()

        total_product_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "total_product"))).text
        total_shipping_price = self.driver.find_element_by_id("total_shipping").text

        float_total_product_price = float(total_product_price[1:])

        assert_that(float_total_product_price, less_than_or_equal_to(20))
        assert_that("$2", is_in(total_shipping_price))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
