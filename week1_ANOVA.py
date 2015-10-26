# Course: Data Analysis
# Week1
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

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

## Group by mean
ipp_mean = df3['incomeperperson'].dropna().mean()

def meangroup (row):
    if row['incomeperperson'] >=ipp_mean:
        return 1
    elif row['incomeperperson'] < ipp_mean:
        return 0
        
df3['meangroup'] = df3.apply(lambda row : meangroup(row),axis=1)
c3= df3.groupby('meangroup').size()



# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='femaleemployrate ~ C(meangroup)', data=df3)
results1 = model1.fit()
print (results1.summary())

# Run MultiComparison using \Tukey
df3['qcut'] = pd.qcut(df3.incomeperperson, 4, labels=["1","2","3","4"]).dropna()
sub1 = df3[['incomeperperson', 'femaleemployrate', 'qcut']].dropna()
mc1 = multi.MultiComparison(sub1['femaleemployrate'], sub1['qcut'])
res1 = mc1.tukeyhsd()
print(res1.summary())

print (sub1.groupby('qcut').mean())
