from selenium import webdriver
from selenium.webdriver.common.by import By # Responsible for different locator strategies

driver = webdriver.Chrome()

# ----------------------------------------------------------------------
# 0. REPEAT EVERYTHING I CODED DURING THE CLASS.
















# ----------------------------------------------------------------------
# 1. FIND THE MOST OPTIMAL LOCATORS FOR CREATE ACCOUNT (REGISTRATION) PAGE ELEMENTS


# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Create account text
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# Your name input field
driver.find_element(By.ID, 'ap_customer_name')

# Email input field
driver.find_element(By.ID, 'ap_email')

# Password input field
driver.find_element(By.ID, 'ap_password')

# Passwords must be at least 6 characters.
driver.find_element("div.auth-inlined-information-message div.a-alert-content")
# fix inside the ()

# Re-enter password input field
driver.find_element(By.ID, 'ap_password_check')

# Create you Amazon account button
driver.find_element(By.ID, 'continue')

# Conditions of Use link
driver.find_element(By.XPATH. "//div[@id='legalTextRow'] / a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice link
driver.find_element(By.XPATH. "//div[@id='legalTextRow'] / a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Sign in link
driver.find_element()













# ----------------------------------------------------------------------
# 2. Update a test case for support search using BDD. User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)










# ----------------------------------------------------------------------
# 3. CREATE A TEST CASE USING BDD THAT OPENS AMAZON.COM, CLICKS ON THE CART ICON AND VERIFIES THAT YOUR AMAZON CART IS EMPTY.

