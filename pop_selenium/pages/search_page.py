from selenium.webdriver.common.by import By
from pop_selenium.pages.base_page import BasePage


class SearchPage(BasePage):

    product_element = (By.XPATH, "//div[@class='right-block']//a[@class='product-name'][contains(text(),'{}')]")
    add_to_cart_button = (By.XPATH, "//*[@title='Add to cart']")
    proceed_button = (By.XPATH, "//*[@title='Proceed to checkout']")
    continue_button = (By.XPATH, "//*[@title='Continue shopping']")

    def add_to_basket(self, name=None):
        self.hover_element(*self.product_element, name)
        self.driver.find_element(*self.add_to_cart_button).click()
        self.wait_until_clickable(*self.continue_button)

    def proceed_to_checkout(self):
        self.wait_until_clickable(*self.proceed_button)


