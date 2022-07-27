import pandas as pd
import re

pd.set_option('display.max_rows', None)



df=pd.read_csv(f'/home/ubuntu/italaw_docfiles.csv', names=["case","link"])
# if df['case'].str.extract(r'\(formerly(.+?)\)') is not np.nan:
#     df['case_clean1']=df['case'].str.extract(r'\(formerly(.+?)\)')
# else: 
#     df['case_clean1']=df['case']

df['case_clean1']=df['case'].str.replace(r'\(formerly(.+?)\)','' ,regex=True)
                                    
print(df)