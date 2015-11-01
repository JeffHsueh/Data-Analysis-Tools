# Course: Data Analysis Tools
# Week2
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np
import seaborn
import scipy.stats
import matplotlib.pyplot as plt

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

#cut into 4 groups
df3['income4groups'] = pd.qcut(df3.incomeperperson, 4, labels=["Terrible","Bad","Decent","Great"]).dropna()
df3['income4groups'] = df3['income4groups'].astype('category')
df3['polityscore'] = df3['polityscore'].astype('category')
#ct1 =  df3.groupby('income4groups').mean()
#print (ct1)

# contingency table of observed counts
ct2=pd.crosstab(df3['polityscore'] , df3['income4groups'])
print (ct2)

# column percentages
colsum=ct2.sum(axis=0)
colpct=ct2/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)

# new code for setting variables to numeric:
df3['polityscore'] = df3['polityscore'].convert_objects(convert_numeric=True)

# graph percent with nicotine dependence within each smoking frequency group 
seaborn.factorplot(x="income4groups", y="polityscore", data=df3, kind="bar", ci=None)
plt.xlabel('income4groups')
plt.ylabel('polityscore')
plt.show()



# Terrible vs. Bad
recode1 ={'Terrible': 'Terrible', 'Bad':'Bad'}
df3['terriblevsbad'] = df3['income4groups'].map(recode1)
ct3 = pd.crosstab(df3['polityscore'], df3['terriblevsbad'])
colsum= ct3.sum(axis=0)
colpct = ct3/colsum
print ('Terrible vs. Bad\nchi-square value, p value, expected counts')
cs3= scipy.stats.chi2_contingency(ct3)
print (cs3)

# Terrible vs Decent
recode2 ={'Terrible': 'Terrible', 'Decent':'Decent'}
df3['terriblevsdecent'] = df3['income4groups'].map(recode2)
ct4 = pd.crosstab(df3['polityscore'], df3['terriblevsdecent'])
colsum= ct4.sum(axis=0)
colpct = ct4/colsum
print ('Terrible vs Decent\nchi-square value, p value, expected counts')
cs4= scipy.stats.chi2_contingency(ct4)
print (cs4)

#Terrible vs. Great
recode3 ={'Terrible': 'Terrible', 'Great':'Great'}
df3['terriblevsgreat'] = df3['income4groups'].map(recode3)
ct5 = pd.crosstab(df3['polityscore'], df3['terriblevsgreat'])
colsum= ct5.sum(axis=0)
colpct = ct5/colsum
print ('Terrible vs. Great\nchi-square value, p value, expected counts')
cs5= scipy.stats.chi2_contingency(ct5)
print (cs5)

#Bad vs. Decent
recode4 ={'Bad': 'Bad', 'Decent':'Decent'}
df3['badvsdecent'] = df3['income4groups'].map(recode4)
ct6 = pd.crosstab(df3['polityscore'], df3['badvsdecent'])
colsum= ct6.sum(axis=0)
colpct = ct6/colsum
print ('Bad vs. Decent\nchi-square value, p value, expected counts')
cs6= scipy.stats.chi2_contingency(ct6)
print (cs6)

# Bad vs Great
recode5 ={'Bad': 'Bad', 'Great':'Great'}
df3['badvsgreat'] = df3['income4groups'].map(recode5)
ct7 = pd.crosstab(df3['polityscore'], df3['badvsgreat'])
colsum= ct7.sum(axis=0)
colpct = ct7/colsum
print ('Bad vs Great\nchi-square value, p value, expected counts')
cs7= scipy.stats.chi2_contingency(ct7)
print (cs7)

# Decent vs Great
recode6 ={'Decent':'Decent', 'Great':'Great'}
df3['decentvsgreat'] = df3['income4groups'].map(recode6)
ct8 = pd.crosstab(df3['polityscore'], df3['decentvsgreat'])
colsum= ct8.sum(axis=0)
colpct = ct8/colsum
print ('Decent vs Great\nchi-square value, p value, expected counts')
cs8= scipy.stats.chi2_contingency(ct8)
print (cs8)
