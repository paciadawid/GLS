from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import *
option = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://automationpractice.com/")

driver.find_element_by_xpath("//input[@id='search_query_top']").send_keys("test")
driver.find_element_by_xpath("//button[@name='submit_search']").click()

warning_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-warning"))) #.send_keys("test_message")

text_box = warning_box.text

assert_that("test", is_in(text_box))

driver.quit()