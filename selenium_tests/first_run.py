from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

option = webdriver.FirefoxOptions()

# option.add_argument("--start-maximized")  -> not working for Firefox

driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("http://automationpractice.com/")

driver.find_element_by_class_name("login")

driver.quit()

_protected = 1
__private = 1
