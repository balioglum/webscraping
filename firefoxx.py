from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('http://example.com')
html = browser.page_source
print(html)