from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:  # equal to class BasePage(object)

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def hover_element(self, by_method: By, value: str, name=None):
        if name:
            value = value.format(name)
        sleep(0.5)
        print(value)
        product = self.driver.find_element(by_method, value)
        sleep(0.5)
        hover = ActionChains(self.driver).move_to_element(product)
        sleep(0.5)
        hover.perform()
        sleep(0.5)

    def wait_until_visible(self, by_method: By, value: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_method, value)))

    def wait_until_clickable(self, by_method: By, value: str):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by_method, value))).click()

    def get_text_from_element(self, by_method: By, value: str):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_method, value))).text
