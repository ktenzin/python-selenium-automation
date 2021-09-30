from selenium import webdriver
from selenium.webdriver.common.by import By # Responsible for different locator strategies

driver = webdriver.Chrome()

# LINK TO TEST SCRIPT
# https://github.com/ktenzin/python-selenium-automation/blob/master/homework/hw_lesson02_amazon_script.py

# ----------------------------------------------------------------------
# 1. REPEAT EVERYTHING I CODED DURING THE CLASS.

# By ID

driver.find_element(By.ID, 'nav-search-submit-button')

driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH

# by href attribute
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

# by class attribute
driver.find_element(By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")

# Search by multiple attributes using 'and'
driver.find_element(By.XPATH, "//a[@data-csa-c-type='link' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']") # using multiple attributes. href is way too long.

# Search by text using 'text()'
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @data-csa-c-type='link']"

# Search across direct child elements: /
driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Best Sellers']")
# / is for direct child

# Search across multiple child elements and their children: //
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
# // is for child at any level

# Contains, contains(attribute, 'partial value')
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(text(), 'Best Sellers')]")
# Use this instead of deprecated By Link Text and By Partial Link Text



# ----------------------------------------------------------------------
# 2. PRACTICE WITH LOCATORS

# Amazon logo
driver.find_element(By.XPATH, "//div[@id='a-page']//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# *Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_condition_of_use')])
# Be careful with text search due to language/localization
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[text()='Conditions of Use']")
# Could also do by href, but it's very long and possibly dynamically generated
# driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-text-center a-size-mini']/a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")
# driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-text-center a-size-mini']//a[contains(text(), 'Conditions of Use')]")

# *Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_privacy_notice')])
# Be careful with text search due to language/localization
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[text()='Privacy Notice']")
# Could also do by href, but it's very long and possibly dynamically generated
# driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-text-center a-size-mini']/a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")


# ----------------------------------------------------------------------
# 3. CREATE A TEST CASE FOR HELP SEARCH USING PYTHON & SELENIUM SCRIPT

# Link to test case:
# https://github.com/ktenzin/python-selenium-automation/blob/master/homework/hw_lesson02_amazon_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/keisharoberts/Documents/GitHub, Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/gp/help/customer/display.html")

# enter search criteria
search = driver.find_element(By.XPATH, "//form[@id='search-help']//input[@name='help_keywords']")
search.clear()
search.send_keys('Cancel order')

# press enter
search.send_keys(Keys.RETURN)

# verify
actual_result = driver.find_element(By.XPATH, "//h1[contains(text(), 'Cancel Items or Orders')]").text
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f'Error. The actual result ({actual_result}) does not match expected result ({expected_result}).'

if actual_result == expected_result:
    print('Test Passed')

# quit driver
driver.quit()







