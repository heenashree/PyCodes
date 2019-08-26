## reset_index -> it reset index of a dataframe

'''
Syntax:
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”)

Parameters:
level: int, string or a list to select and remove passed column from index.
drop: Boolean value, Adds the replaced index column to the data if False.
inplace: Boolean value, make changes in the original data frame itself if True.
col_level: Select in which column level to insert the labels.
col_fill: Object, to determine how the other levels are named.

Return type: DataFrame

'''
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