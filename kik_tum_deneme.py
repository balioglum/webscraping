from contextlib import closing
from selenium import webdriver
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By


opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)



url="https://ekap.kik.gov.tr/EKAP/Ortak/IhaleArama/index.html"
print(browser.get(url))
# use firefox to get page with javascript generated content
with closing(Firefox()) as browser:
     
     browser.get(url)
     button = browser.findElement(By.xpath("//*[@id='pnlFiltreBtn']/button"))
#.find_element_by_name('button')
     button.click()
     # wait for the page to load
     WebDriverWait(browser, timeout=10).until(
         lambda x: x.find_element_by_id('sonuclar'))
     # store it to string variable
     page_source = browser.page_source
print(page_source)