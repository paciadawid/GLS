from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

option = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("http://automationpractice.com/")

# find_elements_by_***
driver.find_element_by_id("header_logo")
driver.find_element_by_class_name("shopping_cart")
driver.find_element_by_id("newsletter-input")
driver.find_element_by_class_name("twitter")
driver.find_element_by_class_name("homefeatured")
driver.find_element_by_id("contact-link")

# CSS selectors
driver.find_element_by_css_selector("#header_logo")
driver.find_element_by_css_selector(".shopping_cart > a")
driver.find_element_by_css_selector('input#newsletter-input[name="email"]')
driver.find_element_by_css_selector(".twitter > a")
driver.find_element_by_css_selector(".homefeatured")
driver.find_element_by_css_selector("nav > #contact-link")

# xpath selectors
driver.find_element_by_xpath("//div[@id='header_logo']")
driver.find_element_by_xpath("//div[@class='shopping_cart']/a")
driver.find_element_by_xpath("//input[@name='email']")
driver.find_element_by_xpath("//*[@class='twitter']/a")
driver.find_element_by_xpath("//*[@class='homefeatured']")
driver.find_element_by_xpath("//nav/*[@id='contact-link']")

driver.quit()

