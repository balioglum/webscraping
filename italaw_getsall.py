import requests
from bs4 import BeautifulSoup
import re
import pprint
import csv

html = '''<div id="hour3"> 
  <div id="day0" class="hour3"> 
    <div class="row first"> 
      <div class="label">Time</div> 
      <div style="font-size: 12px;">14:00</div> 
      <div style="font-size: 12px;">17:00</div> 
    </div> 
    <div class="row wd"> 
      <div class="label h3_wd">Temperature</div> 
      <div>27.5 </div> 
      <div>27.8 </div> 
    </div> 
  <div id="day1" class="hour3"> 
    <div class="row first"> 
      <div class="label">Time</div> 
      <div style="font-size: 12px;">8:00</div> 
      <div style="font-size: 12px;">11:00</div> 
    </div> 
    <div class="row wd"> 
      <div class="label h3_wd">Temperature</div> 
      <div>27.5 </div> 
      <div>27.8 </div> 
    </div>'''

#soup = BeautifulSoup(html, 'html.parser')
for i in range(2015, 2016):
    html = requests.get(f'https://www.italaw.com/browse/chronological?field_case_document_date_value%5Bvalue%5D%5Byear%5D={i}').content
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    link = []

# To convert a list to dictionary, we can use list comprehension and make a key:value pair of consecutive elements. 
# Finally, typecase the list to dict type. 
    def convert(lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct

    header_info = ['filename', 'filelink']
    # öncelikle tekrarlanan en büyük divi seç, table row gibi aynı
    # ,limit=16):
    for row in soup.select('#content > div > div > div.view-content > div.views-row'):
        # tarih seçiyor
        # content attributenın valuesunu alıyorum
        date = row.find('span', {'class': 'date-display-single'})['content']
        case = row.find(
            'div', {'class': 'views-field-field-case-citation'}).get_text()
        # doc=row.select_one("div[class^=views-field-field-case-doc]")#.get_text()
        doc = row.select_one(
            'div.views-field.views-field-field-case-doc-file,div.views-field.views-field-field-case-document-no-pdf')
        # for doc_link in row.select('div.views-field.views-field-field-case-doc-file,div.views-field.views-field-field-case-document-no-pdf').find_all('a'):
        # doc_link=row.select('div.views-field.views-field-field-case-doc-file,div.views-field.views-field-field-case-document-no-pdf')

        #     doc_link=doc_link.get('href')
        doc_link = doc.select(
            'div.views-field.views-field-field-case-doc-file a,div.views-field.views-field-field-case-document-no-pdf a')
        # doc_link tüm a ları ve textlerini getiriyor, list
        for m in doc_link:
            try:
                dname = (m.contents[0])
                dlink = m.get('href')

                link.append(f"{case.strip()}_{dname}")
                link.append(dlink)
                wr = convert(link)
                print(wr)
                print(type(wr))
                with open('italaw_docfiles_2015.csv', 'a') as f:
                    writer = csv.writer(f)
                    for key, value in wr.items():
                        writer.writerow([key, value])
            except IndexError:
                pass
            continue
        with open('italaw_docfiles.csv', 'a') as f:
             writer = csv.writer(f)
             for key, value in wr.items():
                writer.writerow([key, value])
        link = []
         
          # link.append(m)
    # print(f"{case.strip()},{date.strip()},{convert(link)}")

    # pprint.pprint(convert(link))

# {doc.get_text()},{link}


# soup = BeautifulSoup(html, 'html.parser')

# result = {}
# for day in soup.find_all('div', attrs = {'class': 'hour3'}):
#     times = day.find('div', {'class': 'row first'}).find_all('div')
#     temps = day.find('div', {'class': 'row wd'}).find_all('div')
#     result[day.get('id')] = [
#         {'Time': t.text, 'Temperature': temp.text}
#         for t, temp in zip(times[1:], temps[1:])
#     ]
#
