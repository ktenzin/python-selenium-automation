from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Amazon cart')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
