from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    proceed_button = (By.XPATH, "//*[@title='Proceed to checkout']")
    add_to_cart_button = (By.XPATH, "//*[@title='Add to cart']")
    product_element = (By.CLASS_NAME, "product-container")

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def add_to_basket(self):
        product = self.driver.find_element(*self.product_element)
        hover = ActionChains(self.driver).move_to_element(product)
        hover.perform()
        self.driver.find_element(*self.add_to_cart_button).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.proceed_button)).click()
