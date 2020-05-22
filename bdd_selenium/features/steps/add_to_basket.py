from behave import *
from hamcrest import *


@when('I search {item}')
def step_impl(context, item):
    context.home_page.search_item(item)


@step("I add {item} to the basket")
def step_impl(context, item):
    context.search_page.add_to_basket(item)
    context.search_page.proceed_to_checkout()


@then('total price should be smaller than {price}')
def step_impl(context, price):
    total_price = context.summary_page.get_total_price()
    assert_that(total_price, less_than_or_equal_to(float(price)))


@step('shipping price should be {price}')
def step_impl(context, price):
    shipping_price = context.summary_page.get_shipping_price()
    assert_that(shipping_price, equal_to(float(price)))
