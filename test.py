from selenium import webdriver

cchrome_options = webdriver.ChromeOptions()
cchrome_options.add_argument('--headless')
cchrome_options.add_argument('--no-sandbox')
cchrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=cchrome_options)


driver.get("https://m2gcloud.lockular.ai/")


driver.implicitly_wait(200)  # Adjust the timeout as needed

# Fetch the HTML data
html_data = driver.page_source

# Print or process the HTML data as desired
print(html_data)

# Close the browser
driver.quit()