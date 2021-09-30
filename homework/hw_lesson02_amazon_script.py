from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# testing...

# init driver
driver = webdriver.Chrome(executable_path='/Users/keisharoberts/Documents/GitHub, Automation/python-selenium-automation/chromedriver')

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
