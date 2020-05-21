from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    search_field = (By.XPATH, "//input[@id='search_query_top']")
    submit_button_search = (By.XPATH, "//button[@name='submit_search']")

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def search_item(self, item_name):
        self.driver.find_element(*self.search_field).send_keys(item_name)
        self.driver.find_element(*self.submit_button_search).click()
