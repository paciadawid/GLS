from behave import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pop_selenium.pages.home_page import HomePage
from pop_selenium.pages.search_page import SearchPage
from pop_selenium.pages.summary_page import SummaryPage
from allure_behave.hooks import allure_report


allure_report("result")


def before_all(context):
    option = webdriver.FirefoxOptions()
    context.driver = webdriver.Firefox(options=option, executable_path=GeckoDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("http://automationpractice.com/")
    context.home_page = HomePage(context.driver)
    context.search_page = SearchPage(context.driver)
    context.summary_page = SummaryPage(context.driver)


def after_all(context):
    context.driver.quit()
