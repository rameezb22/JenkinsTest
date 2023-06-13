from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set up the desired capabilities
capabilities = DesiredCapabilities.CHROME

# Set up the remote WebDriver
driver = webdriver.Remote("https://jenkins.lockular.in:4444/wd/hub", capabilities)