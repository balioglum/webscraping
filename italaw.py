import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.italaw.com/browse/chronological?field_case_document_date_value%5Bvalue%5D%5Byear%5D=2016').content
soup = BeautifulSoup(html, 'html.parser')
#rows = soup.find_all("div", {"class": "views-row"}, limit=6)
rows= soup.select("div.views-field.views-field-field-case-document-date > div > span.day > span")

product_new=[]
#print (rows)
for row in rows:
    column = row.text#soup.find("div", {"class":"vinayak"}).get_text()
    # if column:
    #     product_new.append(column.get_text(strip=True))
    #     print(product_new)
    print(column)
    #print(a)
    # title = column.a.text
    # year = column.span.text
    # link = column.a['href']
    
    # movie_page = requests.get(f'https://www.imdb.com/{link}').content
    # movie_soup = BeautifulSoup(movie_page, 'html.parser')
    # genre_list = movie_soup.find_all('a', 'sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt')
    # genres = [genre.text for genre in genre_list]
    # print(f'{title} {year} - {genres}')
    