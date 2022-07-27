import pandas as pd
import re

pd.set_option('display.max_rows', None)



df=pd.read_csv(f'/home/ubuntu/italaw_docfiles.csv', names=["case","link"])
# if df['case'].str.extract(r'\(formerly(.+?)\)') is not np.nan:
#     df['case_clean1']=df['case'].str.extract(r'\(formerly(.+?)\)')
# else: 
#     df['case_clean1']=df['case']

#df['case_clean1']=df['case'].str.replace(r'\(formerly(.+?)\)','' ,regex=True)
new_value = {
   'case': {
      r'\(formerly(.+?)\)':'',
      r'\(case formerly(.+?)\)':'',
      r'/':''
    }
}

# new_value ya göre sadece case kolonunu regexle temizleyip, case_New adında yeni kolon ekliyor
# df.iloc[:,0] -> sadece case kolonuna bakıyor
# .to_frame(name='case') -> tek kolonu seriese çevirdiği için case adında yeni sütun isimli dataframe oluşturuyor
# axis=1 sütünlardan yanyana concat et
df_=pd.concat([df,df.iloc[:,0].to_frame(name='case').replace(new_value,regex=True).add_suffix('_New')],axis=1).sort_index(axis=1)


df_.to_csv('italaw_cleaned.csv', header=True, index=False)                               
print(df_)

# ---------------------------------------------------------------------------- #
#                     Pandas replace multiple values regex                     #
# ---------------------------------------------------------------------------- #
# import pandas as pd                                                                                                                                

# df = pd.DataFrame({'City':['Ger-many', 'Eng-land', 'Fr-ance', 'Eng-land', 'Ger-many']})  
# print(df)
# new_value = {
#    'CITY': {
#       r'(G.*Ge|Germany.*)': 'Ger-many',
#       r'E[ng]*[oo]*.*': 'Fraan ce'}
# }

# b= df.replace(new_value, regex=True, inplace=True)
# print(b)
