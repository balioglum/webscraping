import requests
from bs4 import BeautifulSoup
import csv


# To convert a list to dictionary, we can use list comprehension and make a key:value pair of consecutive elements. 
# Finally, typecase the list to dict type. 
def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

for i in range(1850, 2023):
    html = requests.get(f'https://www.italaw.com/browse/chronological?field_case_type_tid%5B%5D=1717&field_case_type_tid%5B%5D=1687&field_case_type_tid%5B%5D=1090&field_case_type_tid%5B%5D=1703&field_case_type_tid%5B%5D=1702&field_case_type_tid%5B%5D=1714&field_case_type_tid%5B%5D=1091&field_case_type_tid%5B%5D=1092&field_case_type_tid%5B%5D=1093&field_case_type_tid%5B%5D=1097&field_case_type_tid%5B%5D=1095&field_case_type_tid%5B%5D=1094&field_case_type_tid%5B%5D=1096&field_case_type_tid%5B%5D=1099&field_case_type_tid%5B%5D=1173&field_case_type_tid%5B%5D=1100&field_case_document_date_value%5Bvalue%5D%5Byear%5D={i}').content
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    link = []



    
    # öncelikle tekrarlanan en büyük divi seç, table row gibi aynı
    # ,limit=16):
    for row in soup.select('#content > div > div > div.view-content > div.views-row'):
        # tarih seçiyor
        # content attributenın valuesunu alıyorum
        date = row.find('span', {'class': 'date-display-single'})['content']
        case = row.find(
            'div', {'class': 'views-field-field-case-citation'}).get_text().replace('\n', '')
        #Strategic Infrasol Foodstuff LLC davasında gereksiz bir newline koyuyor, bunu düzeltmek için .replace('\n', '') 
        doc = row.select_one(
            'div.views-field.views-field-field-case-doc-file,div.views-field.views-field-field-case-document-no-pdf')
        
        doc_link = doc.select(
            'div.views-field.views-field-field-case-doc-file a,div.views-field.views-field-field-case-document-no-pdf a')
        # doc_link tüm a ları ve textlerini getiriyor, list
        #m -><a href="https://www.italaw.com/sites/default/files/case-documents/italaw4092.pdf" target="_blank">Decision on Annulment (English)</a>
        #m.contents ->['Decision on Annulment (English)'] link texti bu, list halinde getiriyor,
        #m.contents[0] -> Decision on Annulment (English)
        for m in doc_link:
            try:
                dname = (m.contents[0])
                dlink = m.get('href')

                link.append(f"{case.strip()}_{dname}")
                link.append(dlink)
                wr = convert(link)
                print(wr)
                print(type(wr))
                with open('italaw_docfiles.csv', 'a') as f:
                    writer = csv.writer(f)
                    for key, value in wr.items():
                        writer.writerow([key, value])
            except IndexError:
                pass
            continue
        link = []
