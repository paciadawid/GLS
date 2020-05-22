from selenium import webdriver
from pop_selenium.selectors.home_page_selecotrs import *

class HomePage:

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def search_item(self, item_name):
        self.driver.find_element(*search_field).send_keys(item_name)
        self.driver.find_element(*submit_button_search).click()
