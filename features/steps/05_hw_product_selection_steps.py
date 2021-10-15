from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page2')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify user can click through product colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Aluminum Grey', 'Ash/Mamba Black', 'Basanite/Eclips', 'Black', 'Cosmic Red', 'Dream Purple',
                       'Plants Print Nieve Green', 'Teakwood Yellow', 'Tortuga/Dustmoss', 'Umber Orange/Ve',
                       'Wave Blue']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error. Expected {expected_colors[i]} did not match actual {current_color}'
