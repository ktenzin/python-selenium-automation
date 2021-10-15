from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('Store product name')
def get_product_name(context):
    context.current_product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.current_product_name}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)

# ----------------------------------------------------------
# TESTING WITH LOOP EXAMPLE 1 -- Straight forward method
# ----------------------------------------------------------
# @then('Verify user can click through colors')
# def verify_can_click_through_colors(context):
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#     for color in colors:
#         color.click()

# TESTING WITH LOOP EXAMPLE 2 -- Add an array with color options
# Loop dynamically
@then('Verify user can click through colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Dark Navy', 'Black', 'Dusty Rose']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error. Expected {expected_colors[i]} did not match actual {current_color}'


# TESTING WITH LOOP EXAMPLE 3 -- Click through every color and compare the actual text
# Here, we click on the color and grab the value for each color, then compare that list to our expected list.
# @then('Verify user can click through colors')
# def verify_can_click_through_colors(context):
#     expected_colors = ['Dark Navy', 'Black', 'Dusty Rose']
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#     actual_colors = []
#
#     for color in colors:
#         color.click()
#         actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
#         print(f'Actual colors: {actual_colors}')
#
#     assert expected_colors == actual_colors, f'Error. Expected color {expected_colors} did not match {actual_colors}.'
