#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

df_train=pd.read_csv("HEART.csv")
print(df_train)


# In[51]:


#Display attributes in the data set.
attribute=[]
#check the decoration
attribute=df_train.columns
print(attribute)
print(len(attribute))


# In[68]:


#Describe the attributes name, count no of values, and find min, max, data type, range, quartile, percentile, box plot and outliers.
for x in attribute:
#descriptive statistics summary
    print(df_train[x].describe())
    print(" ")


# In[76]:


#Describe the attributes name, count no of values, and find min, max, data type, range, quartile, percentile, box plot and outliers.
for x in attribute:    
    #Boxplot
    sns.boxplot(df_train[x])
    sns.despine()


# In[92]:


#Give visualization of statistical description of data – in form of histogram, scatter plot, pie chart
#histogram
for x in attribute:
    plt.hist(df_train[x])
    plt.title(x)
    plt.show()


# In[89]:


#Give visualization of statistical description of data – in form of histogram, scatter plot, pie chart
#scatterplot
for x in attribute:
    plt.scatter(df_train[x],df_train[x])
    plt.xlabel(x)
    plt.ylabel(x)
    plt.show()


# In[ ]:


#Give visualization of statistical description of data – in form of histogram, scatter plot, pie chart
#piechart
for x in attribute:
    test=df_train.groupby([x]).count()
    print(type(test))
    for i in test:
        plt.pie(test[i],labels=test[i])
        plt.title(x)
        plt.show()
       


# In[80]:


#correlation matrix
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)


# In[67]:


#Identify missing values and outlier and fill them with average. 
for x in attribute:
    #Using numpy mean function to calculate the mean value
    meanAge = np.mean(df_train[x])
 #replacing missing values in the DataFrame
    df_train[x] = df_train[x].fillna(meanAge)

