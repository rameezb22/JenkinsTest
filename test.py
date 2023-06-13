from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://sabien-dasbhoard.lockular.ai/")