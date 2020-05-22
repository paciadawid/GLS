from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SummaryPage:

    search_field = (By.ID, "total_product")
    submit_button_search = (By.ID, "total_shipping")

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_total_price(self):
        total_product_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "total_product"))).text
        return float(total_product_price[1:])

    def get_shipping_price(self):
        total_shipping_price = self.driver.find_element_by_id("total_shipping").text
        return float(total_shipping_price[1:])
