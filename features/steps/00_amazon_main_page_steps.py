from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a.nav_a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a[data-nav-role='signin']")


# -- LESSON 5 EXAMPLE ------------------------
@when('Click Sign In from popup')
def click_sign_in_popup(context):
    context.driver.wait = WebDriverWait(context.driver, 10)
    # context.driver.wait.until(
    #     EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Sign in btn not clickable'
    # ).click()
    e = context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Sign in btn not clickable')
    e.click()


# -- PREVIOUS LESSON EXAMPLES ----------------


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {search_word} into amazon search1')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


# find_element will throw an exception if the element is not found.
# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     context.driver.find_element(*HAM_MENU_ICON)


@then('Verify hamburger menu icon is present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON)


# find_elements will NOT throw an exception if the element is not found.
# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     context.driver.find_elements(*HAM_MENU_ICON)


# If using find_elements, you must ALWAYS COUNT ELEMENTS to verify everything is correct.
# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     expected_count = 1
#     actual_count = len(context.driver.find_elements(*HAM_MENU_ICON))
#     assert expected_count == actual_count, f'Actual elements {actual_count}, but expected {expected_count}.'


# If you want to print results to compare find_element vs find_elements
# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     print('\nFIND ELEMENT:\n')
#     element = context.driver.find_element(*HAM_MENU_ICON)
#     print(element)
#     print(type(element))
#
#     print('\nFIND ELEMENTSSSS:\n')
#     elements = context.driver.find_elements(*HAM_MENU_ICON)
#     print(elements)
#     print(type(elements))

    # expected_count = 1
    # actual_count = len(context.driver.find_elements(*HAM_MENU_ICON))
    # assert expected_count == actual_count, f'Actual elements {actual_count}, but expected {expected_count}.'


@then('Verify {expected_amount} footer links are present')
def verify_footer_links_count(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(links)}'
    # TO PRINT THE LINKS AS CODE
    # print(links)
    # TO PRINT THE 6TH LINK AS TEXT
    # print(links[5].text)
    # TO PRINT THE 6TH LINK.
    # print(links[5])
    # TO CLICK THE 6TH LINK. CAN ADD WAIT.
    # links[5].click()
    # TO PRINT ALL OF THE LINKS
    # for l in links:
    #     print(l.text)

