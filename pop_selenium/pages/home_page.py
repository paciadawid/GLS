from pop_selenium.selectors.home_page_selecotrs import *
from pop_selenium.pages.base_page import BasePage


class HomePage(BasePage):

    def search_item(self, item_name):
        self.driver.find_element(*search_field).clear()
        self.driver.find_element(*search_field).send_keys(item_name)
        self.wait_until_clickable(*submit_button_search)
