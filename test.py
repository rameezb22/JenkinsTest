from selenium import webdriver

DesiredCapabilities capability = DesiredCapabilities.chrome();

WebDriver driver = new RemoteWebDriver(new URL("https://jenkins.lockular.in:4444/wd/hub"), capability);
