import pandas as pd
#read in only columns 0 (title) and 11 (URL)

myCSV = pd.read_csv('matched-titles-in-ethos.txt', usecols=[0,11])

myCSV.to_csv('pandas-out.txt', encoding='utf-8', sep='#', index=False)



