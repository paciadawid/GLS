from selenium.webdriver.common.by import By
from pop_selenium.pages.base_page import BasePage


class SearchPage(BasePage):

    product_element = (By.CLASS_NAME, "product-container")
    add_to_cart_button = (By.XPATH, "//*[@title='Add to cart']")
    proceed_button = (By.XPATH, "//*[@title='Proceed to checkout']")

    def add_to_basket(self):
        self.hover_element(*self.product_element)
        self.driver.find_element(*self.add_to_cart_button).click()
        self.wait_until_clickable(*self.proceed_button)
