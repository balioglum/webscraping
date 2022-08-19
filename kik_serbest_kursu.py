import requests
from bs4 import BeautifulSoup
import re
import time
from pprint import pprint
import pandas as pd
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

df = pd.DataFrame(columns=['adsoyad', 'tarih','baslik', 'metin'])
#for page in range(1,2):
browser.get(f'https://www.ihale.gov.tr/SerbestKursu.aspx')#f"https://www.ihale.gov.tr/SerbestKursu.aspx#sayfa-{page}"

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "html.parser")

        
lists = soup.select("li.ustYorum")
print(lists)
for lis in lists:
    adsoyad = lis.find('div', class_="yorumAdSoyad").text
    tarih = lis.find('div', class_="yorumTarih").text
    baslik = lis.select_one('div:nth-child(4)', class_="yorumBaslik").text
    metin = lis.select_one('div:nth-child(6)', class_="yorumBaslik").get_text().replace('\n', '').replace(",","")
    #metin=metin.replace(",","")
    #info = [adsoyad, tarih,baslik, metin]
    a={'adsoyad': adsoyad,'tarih': tarih,'baslik': baslik,'metin': metin}
    a = pd.DataFrame.from_dict([a])
    df = pd.concat([df,a],ignore_index=True, axis=0)
print(df)
df.to_csv("/home/ubuntu/webscraper/kik.csv", index=False, encoding='utf-8-sig', sep='|')