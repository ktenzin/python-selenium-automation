from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Init driver
driver = webdriver.Chrome(executable_path='/Users/keisharoberts/Documents/GitHub, Automation/python-selenium-automation/chromedriver')

# Open page
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# Enter search
driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)

# Verify
actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Test failed. Expected: {expected_text}, but got: {actual_text}.'


# Close window
driver.quit()
