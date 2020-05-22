from selenium.webdriver.common.by import By
from pop_selenium.pages.base_page import BasePage


class SummaryPage(BasePage):

    product_price_selector = (By.ID, "total_product")
    shipping_price_selector = (By.ID, "total_shipping")

    def get_total_price(self):
        total_product_price = self.get_text_from_element(*self.product_price_selector)
        return float(total_product_price[1:])

    def get_shipping_price(self):
        total_shipping_price = self.get_text_from_element(*self.shipping_price_selector)
        return float(total_shipping_price[1:])
