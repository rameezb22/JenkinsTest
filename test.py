

Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox", "http://my.test.site.org/");

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
