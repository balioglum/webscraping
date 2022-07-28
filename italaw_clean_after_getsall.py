import pandas as pd
import re
from pathlib import Path 
import os
import urllib.parse
import sys




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)




df=pd.read_csv(f'/home/ubuntu/italaw_docfiles.csv', names=["case","link"])


# As with other codecs, serialising a string into a sequence of bytes is known as encoding, 
# and recreating the string from the sequence of bytes is known as decoding.
# iso-8859-9 türkçe ve ispanyolca karakterlere uygun.
#önce encode ile bytelarına ayırıyor, iso-8859-9 a uymayan u200b vs bunları ignore edip sonra decode ile birleştiriyor!
df['case']=[s.encode('iso-8859-9', 'ignore').decode("iso-8859-9") for s in df['case']]

new_value = {
   'case': {
      r' \(formerly(.+?)\)':'',
      r' \(also(.+?)\)':'',
      r' \(case formerly(.+?)\)':'',
      r'/':'-',
      r'\"':'',
      r'""':'',
      r' \(\"\"Number 2\"\"\)':'Number 2',
      r' \(English\)':'-En',
      r'  \(French\)':'-Fr',
      r' \(Spanish\)':'-Spn',
      r' \(Swedish\)':'-Swe',
      #r'-':' ',
      r'B\.V\. ':'',
      r'Inc\. ':'',
      r'S\.à r\.l\. ':'',
      r'Sàrl ':'',
      r'’':'',
      r'\'':'',
      r'_ ':'_',
      r' _ ':'_',
      r' _':'_',
      r'; ':'-',
      r' ARB \(AF\)':'ARB(AF)',
      r'([,.])(?=.+v\.)':'' #v. ye kadar olan tüm nokta ve virgülleri sil
   } 
}

# new_value ya göre sadece case kolonunu regexle temizleyip, case_New adında yeni kolon ekliyor
# df.iloc[:,0] -> sadece case kolonuna bakıyor
# .to_frame(name='case') -> tek kolonu seriese çevirdiği için case adında yeni sütun isimli dataframe oluşturuyor
# axis=1 sütünlardan yanyana concat et
df_=pd.concat([df,df.iloc[:,0].to_frame(name='case').replace(new_value,regex=True).add_suffix('_new')],axis=1).sort_index(axis=1)

df_['case_new']=df_['case_new'].str.strip()
df_['link']=df_['link'].apply(urllib.parse.unquote) # %20 olarak görünenleri space'e çeviriyor
df_['filename']=df_['link'].apply(os.path.basename) #path'ten filename çekiyor

def utf8len(s):
    return len(s.encode('utf-8'))

df_['casesize']=df_['case'].apply(sys.getsizeof)
df_['caselength']=df_['case'].apply(len)
df_['caseutf8len']=df_['case'].apply(utf8len)

#x=df_['case'].value_counts()
#print(x)
df_.drop_duplicates(subset=None, inplace=True)
df_['case_folder_name'] = df_['case_new'].str.split(",").str[0]
df_.to_csv('italaw_cleaned.csv', header=True, index=False)                               
print(df_.sort_values(by='caseutf8len', ascending=False).head(10))

df_['case_folder_name'] = df_['case_folder_name'].str.split("_").str[0]
df_folders=df_['case_folder_name'].drop_duplicates().to_frame()


print(df_folders['case_folder_name'])
print(df_folders.info())

#df_folders['case_folder_name']=[(s.encode('ascii', 'ignore')).decode("utf-8") for s in df_folders['case_folder_name']]
df_folders.to_csv('italaw_folders.csv', header=True, index=False)
