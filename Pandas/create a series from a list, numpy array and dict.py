import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

df1 = pd.Series(mylist)
df2 = pd.Series(myarr)
df3 = pd.Series(mydict)
#Print without index df.to_string(index=False)

print(df1, df2.to_string(index=False), df3)
