from selenium.webdriver.common.by import By
from behave import given, then


BENEFIT_BOXES = (By.ID, 'prime-benefit-module-more-content-item')


@given('Open Amazon Prime')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/prime')


@then('Verify {expected_amount} benefit boxes are present')
def verify_benefit_boxes_count(context, expected_amount):
    boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(boxes) == int(expected_amount), f'Expected {expected_amount} boxes, but got {len(boxes)}'
    print(len(boxes))

# Same as above, but USING CONDITIONS
# @then('Verify {expected_amount} benefit boxes are present')
# def verify_benefit_boxes_count(context, expected_amount):
#     boxes = context.driver.find_elements(*BENEFIT_BOXES)
    # assert len(boxes) == int(expected_amount), f'Expected {expected_amount} boxes, but got {len(boxes)}'
    # print(len(boxes))
    # if len(boxes) == expected_amount:
    #     boxes[0].click()




