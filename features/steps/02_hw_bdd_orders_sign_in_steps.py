from selenium.webdriver.common.by import By
from behave import given, when, then
import time

@given('Open Amazon page hw2')
def open_amazon_hw2(context):
    context.driver.get('https://www.amazon.com')


@when('When User clicks orders hw2')
def click_orders(context):
    # context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']//span[@style='visibility: visible;']").click()
    time.sleep(10)
    context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']//span[@class='nav-line-2']").click()