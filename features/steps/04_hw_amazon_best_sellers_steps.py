from selenium.webdriver.common.by import By
from behave import given, then


BEST_SELLER_LINKS = (By.CSS_SELECTOR, '#zg_header li')


@given('Open Amazon Best Sellers1')
def open_amazon_best_sellers1(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.refresh()


@then('Verify {expected_amount} menu Best Sellers menu links are present')
def verify_best_sellers_links_count(context, expected_amount):
    best_sellers_links_count = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(best_sellers_links_count) == int(expected_amount), f'Expected {expected_amount} Best Sellers menu links, but got {len(best_sellers_links_count)}'
    # print(len(best_sellers_links_count))