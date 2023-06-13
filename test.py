from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

cchrome_options = webdriver.ChromeOptions()
cchrome_options.add_argument('--headless')
cchrome_options.add_argument('--no-sandbox')
cchrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=cchrome_options)


driver.get("https://m2gcloud-staging.lockular.ai")


 # Adjust the timeout as needed


username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')


username_input.send_keys('rameezb')
password_input.send_keys('lockular')

password_input.send_keys(Keys.RETURN)

time.sleep(60)

html_data = driver.page_source

# Print or process the HTML data as desired
print(html_data)

# Close the browser
driver.quit()
