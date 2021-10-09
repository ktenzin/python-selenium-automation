from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')


@given('Open Amazon product page 1')
def open_amazon_product_page1(context):
    context.driver.get('https://www.amazon.com/Vessel-Baseline-Tennis-Racquet-Rose/dp/B087JXH46Y/')


@when('Click add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify {product_count} item is in cart')
def verify_cart_count(context, product_count):
    (actual_count) = context.driver.find_element(*CART_COUNT).text
    assert int(actual_count) == int(product_count), f'Error! Expected {product_count} product, but got {actual_count} product.'
