import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)

#for combining 2 series, you can use concatination


df = pd.concat([ser1,ser2])
print(df)

df = pd.concat([ser1,ser2], axis=1)
print(df)