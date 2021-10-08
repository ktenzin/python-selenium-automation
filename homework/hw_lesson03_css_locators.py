from selenium import webdriver
from selenium.webdriver.common.by import By # Responsible for different locator strategies

driver = webdriver.Chrome()

# ----------------------------------------------------------------------
# 1. FIND THE MOST OPTIMAL LOCATORS FOR CREATE ACCOUNT (REGISTRATION) PAGE ELEMENTS

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name input field
driver.find_element(By.ID, 'ap_customer_name')

# Email input field
driver.find_element(By.ID, 'ap_email')

# Password input field
driver.find_element(By.ID, 'ap_password')

# Passwords must be at least 6 characters text
# driver.find_element(By.CSS_SELECTOR, "div.auth-inlined-information-message div.a-alert-content")
driver.find_element(By.CSS_SELECTOR, ".auth-inlined-information-message .a-alert-content")

# Re-enter password field
driver.find_element(By.ID, 'ap_password_check')

# Create your Amazon account button
driver.find_element(By.ID, 'continue')

# Conditions of Use link
# *** QUESTION: Is it ok omit the beginning of the href to shorten it? If that's ok, how much can you cut? ***
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use'])

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/r/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")

# Sign in link
driver.find_element(By.)
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")


# ----------------------------------------------------------------------
# 2. Update a test case for support search using BDD. User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)










# ----------------------------------------------------------------------
# 3. CREATE A TEST CASE USING BDD THAT OPENS AMAZON.COM, CLICKS ON THE CART ICON AND VERIFIES THAT YOUR AMAZON CART IS EMPTY.

