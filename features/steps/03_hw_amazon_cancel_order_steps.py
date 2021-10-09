from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order into Amazon search')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('cancel order', Keys.ENTER)

