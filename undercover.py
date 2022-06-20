import os
import glob
import pandas as pd
 

path = fr"C:\Users\Mehdi Alebrahim\Desktop\test"
 

file_list = glob.glob(path + "/*.xlsx")
 

excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 

excl_merged = pd.DataFrame()
     
 
excl_merged = pd.concat(
    excl_list, ignore_index=True)

excl_merged.to_excel('test_export.xlsx', index=False)

