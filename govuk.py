from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

#example url
url = "https://beta.companieshouse.gov.uk/company/00445790/filing-history"
link_list = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for a in soup.find_all('a', href=True):
    if "document" in a['href']:
        print(a)
        tit=a.select_one('strong').get_text()
        print(tit)
        print(a['href'])
        print('######')
        link_list.append("https://beta.companieshouse.gov.uk"+a['href'])
print(link_list)

for tit, url in enumerate(link_list, 1):
    response = requests.get(url)
    

    with open(f'/home/ubuntu/webcraper/govuk/report_{tit}.pdf', 'wb') as f:
        f.write(response.content)