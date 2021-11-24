from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 3. Create a test case for Help search using python & selenium script
# Test Case:
# User can search for solutions of Cancelling an order on Amazon

# init driver
driver = webdriver.Chrome(executable_path='/Users/keisharoberts/Documents/GitHub, Automation/python-selenium-automation/chromedriver')

# open the url
driver.get("https://www.amazon.com/gp/help/customer/display.html")

# enter search criteria
search_input = driver.find_element(By.ID, 'helpsearch')
search_input.send_keys('Cancel order')
search_input.send_keys(Keys.ENTER)

# verify
actual_result = driver.find_element(By.XPATH, "//h1").text
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f'Error. Actual result {actual_result} does not match {expected_result}.'

# print result
print('Test case passed')

# quit driver
driver.quit()
