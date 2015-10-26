# Course: Data Analysis Tools
# Week1
#Editor: Kuo-Lin Hsueh

import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import Statsmodels


df = pd.read_csv("gapminder.csv", low_memory = False, index_col = 0)
maleemployrate = pd.read_csv("maleemployrate_sub.csv", low_memory = False, index_col = 0)

df["incomeperperson"] = df["incomeperperson"].convert_objects(convert_numeric=True)
df["femaleemployrate"] = df["femaleemployrate"].convert_objects(convert_numeric=True)
df["polityscore"] = df["polityscore"].convert_objects(convert_numeric=True)
df['employrate'] = df['employrate'].convert_objects(convert_numeric=True)

maleemployrate['2007'] = maleemployrate['2007'].convert_objects(convert_numeric=True)


#Concatenate df , df2
df3 =  pd.concat([df, maleemployrate], axis=1, join_axes=[df.index])

df3.rename(columns= {'2007':'maleemployrate'}, inplace=True) #rename column


# Calulating mean for incomeperperson
mean_ipp = (df3["incomeperperson"].mean(skipna=True)) 

country_abovemean = df3.loc[df3["incomeperperson"] >= mean_ipp] # countries having higher income/person than the average
country_belowmean = df3.loc[df3["incomeperperson"] < mean_ipp]  # countries having less income/person than the average

sub1 = country_abovemean.copy()
sub2 = country_belowmean.copy()

# Polity Score bar graph 
sub1["polityscore"] = sub1["polityscore"].astype('category')
sub2["polityscore"] = sub2["polityscore"].astype('category')
