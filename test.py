

#from selenium import webdriver

# Set up the browser driver
#driver = webdriver.Chrome('/path/to/chromedriver')

WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);

# Navigate to the webpage
driver.get('http://example.com')

# Wait for the page to fully load
driver.implicitly_wait(10)  # Adjust the timeout as needed

# Fetch the HTML data
html_data = driver.page_source

# Print or process the HTML data as desired
print(html_data)

# Close the browser
driver.quit()
