
from selenium import webdriver
from selenium.webdriver.common.by import By # Responsible for different locator strategies

driver = webdriver.Chrome()

# ----------------------------------------------------------------------
# 1. FIND THE MOST OPTIMAL LOCATORS FOR CREATE ACCOUNT (REGISTRATION) PAGE ELEMENTS

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account text
driver.find_element(By.CSS_SELECTOR, 'div.a-box-inner h1')

# Your name input field
driver.find_element(By.ID, 'ap_customer_name')

# Email input field
driver.find_element(By.ID, 'ap_email')

# Password input field
driver.find_element(By.ID, 'ap_password')

# Passwords must be at least 6 characters text
driver.find_element(By.CSS_SELECTOR, ".auth-inlined-information-message .a-alert-content")

# Re-enter password field
driver.find_element(By.ID, 'ap_password_check')

# Create your Amazon account button
driver.find_element(By.ID, 'continue')

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition_of_use']")

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='privacy_notice']")

# Sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")