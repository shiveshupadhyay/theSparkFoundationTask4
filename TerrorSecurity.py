#!/usr/bin/env python
# coding: utf-8

# # Shivesh Upadhyay

# ## Looking at data

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv(r'terror.csv',encoding='latin1')
dataset.head(10)


# In[3]:


dataset.columns


# In[4]:


dataset.nunique()


# ### There are too many columns and too many unique values for each column, but by looking at CSV file we get to know that columns : - ('region_txt' , 'country_txt', 'provstate' and 'city') are used for location. So in following we will look the number of terror attacks according to these locations. We will start with column with more specific location but less number of  unique values.

# In[11]:


dataset['region_txt'].unique()


# #### We see region_txt has less unique value but it is too less in number that is a very broader category so we move to country_txt

# In[5]:


dataset["country_txt"].unique()


# #### From above we  see country_txt has fairly large unique values but is  still can be handled in analysis easily  and it is also more specific location than region_txt. So we will look for null values and start our analysis from here only.

# In[25]:


dataset["country_txt"].isnull().sum()


# #### No missing value so green signal to moove ahead

# In[26]:


country = dataset["country_txt"].unique()
count = [] 
for i in country:
    count.append(len(dataset[dataset['country_txt'] == i]))
fig = plt.figure(figsize =(10, 7))
plt.pie(count, labels = country)
plt.show()


# ### From above pie-chart it is evident that  'Iraq' has most terror cases followed by 'Pakistan' and 'India'. But for surity we can check  by code below

# In[27]:


max = 0;
cx = "" 
for i in country:
    if (len(dataset[dataset['country_txt'] == i]) > max):
        max = len(dataset[dataset['country_txt'] == i])
        cx = i
print(cx, max)


# ### Now we will look for provstate inside iraq and then city inside most affected provstate

# In[28]:


d1 = dataset[dataset['country_txt'] == 'Iraq']


# In[29]:


d1['region_txt'].unique()


# In[30]:


d1['provstate'].unique()


# In[31]:


d1['provstate'].isnull().sum()


# In[32]:


x1 = d1['provstate'].unique()
for i in x1:
    print(i , len(d1[d1['provstate'] == i]))


# In[33]:


d2 = d1[d1['provstate'] == 'Baghdad']
x2 = d2['city'].unique()


# In[34]:


d2['city'].isnull().sum()


# In[35]:


for i in x2:
    print(i , len(d1[d1['city'] == i]))


# ## So 'Baghdad' is most terror affected city in world. It may possible if any city in pakistan also has more terror cases. So for surity we will look for it also.

# In[36]:


d3 = dataset[dataset['country_txt'] == 'Pakistan']


# In[37]:


d3['region_txt'].unique()


# In[38]:


d3['provstate'].unique()


# In[39]:


x3 = d3['provstate'].unique()
for i in x3:
    print(i , len(d3[d3['provstate'] == i]))


# ## We can see that not even any provstate in pakistan has cases as much as in Baghdad city.      So 'BAGHDAD' city is most terror affected region in world in my analysis
