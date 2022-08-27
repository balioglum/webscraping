
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)


# move to some url
driver.get('https://ekap.kik.gov.tr/EKAP/Ortak/YeniIhaleAramaData.ashx?ES=&pageIndex=1&metot=ara&tabId=4731503f-a785-4c47-803b-e61f3af28976&iknYil=2020&orderBy=8&yasaKapsami=1&isMobil=1&kayitTuru=1')

driver.quit()
soup = BeautifulSoup(driver.page_source, "html.parser")
# use "scroll" function to scroll the page every 5 seconds

print(soup)
# Scroll function
# This function takes two arguments. The driver that is being used and a timeout.
# The driver is used to scroll and the timeout is used to wait for the page to load.

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

#scroll(driver, 5)