import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from hamcrest import *


class MyTestCase(unittest.TestCase):

    # Once per class
    # def setUpClass(cls):
    #     option = webdriver.FirefoxOptions()
    #     cls.driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
    #     cls.driver.maximize_window()
    #     cls.driver.get("http://automationpractice.com/")

    def setUp(self):
        option = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")

    def test_search_cart(self):
        self.driver.find_element_by_xpath("//input[@id='search_query_top']").send_keys("test")
        self.driver.find_element_by_xpath("//button[@name='submit_search']").click()
        warning_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-warning")))  # .send_keys("test_message")
        text_box = warning_box.text
        assert_that("test", is_in(text_box))

    def test_orders_and_credits(self):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_xpath("//input[@name = 'email']").send_keys("seleniumremote@gmail.com")
        self.driver.find_element_by_xpath("//input[@name = 'passwd']").send_keys("test123" + Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@title='Orders']"))).click()

        box_element = self.driver.find_element_by_css_selector(".alert.alert-warning")
        text_box = box_element.text
        assert_that(text_box(not_(empty())))
        self.driver.back()
        self.driver.find_element_by_xpath("//a[@title='Credit slips']").click()
        self.driver.find_element_by_css_selector(".alert.alert-warning")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
