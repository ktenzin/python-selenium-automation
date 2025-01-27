from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Amazon Cart is empty')
def verify_text_shown(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty").text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}.'
