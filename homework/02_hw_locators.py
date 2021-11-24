from selenium import webdriver
from selenium.webdriver.common.by import By # Responsible for different locator strategies


# LESSON 2 HOMEWORK

# 2. Practice with locators.
# Create locators + search strategy for these page elements of Amazon Sign in page:

# Amazon logo
driver.find_element(By.XPATH, "//div[@id='a-page']//i[@class='a-icon a-icon-logo']")

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
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_desktop_footer_cou?')]")

# *Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_desktop_footer_privacy_notice?')]")