from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify cancel order text is shown')
def verify_text_shown(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".a-color-state.a-text-bold").text
    expected_result = '"cancel order"'
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}.'


# ANOTHER WAY TO DO IT
# @then('Verify {expected_result} search text is shown')
# def verify_text_shown(context, expected_result):
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, ".a-color-state.a-text-bold").text
#     expected_result = '"cancel order"'
#     assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}.'
