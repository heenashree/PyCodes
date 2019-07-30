import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
#print(mydict)
ser = pd.Series(mydict)
df = ser.to_frame().reset_index()
print(df)
#print(df.tail())
#print(df.head())