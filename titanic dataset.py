#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


fd=pd.read_csv("Titanic")
fd


# In[5]:


##top  5 fields
fd.head()


# In[6]:


##Getting the particular record
fd.drop(["PassengerId","Name","Ticket"],axis=1,inplace=True)


# In[ ]:





# In[7]:


fd.head()   


# In[11]:


##countplot
sns.countplot(x="Survived",data=fd)
fd["Survived"].value_counts()
fd["Sex"].value_counts()


# In[8]:


## Displot
sns.displot(fd.Age)


# In[9]:


##count plot by parameters
sns.countplot(x="Survived",hue="Sex",data=fd)


# In[10]:


##count plot by parameters
sns.countplot(x="Survived",hue="Pclass",data=fd)


# In[11]:


## find the correlation 
correlation=fd.corr()
correlation


# In[62]:


## heatmap
sns.heatmap(correlation,annot=True)


# In[12]:


## pairplot
sns.pairplot(fd)


# In[13]:


##Barplot
sns.barplot(x="Survived",y="Age",data=fd)


# In[69]:


sns.barplot(x="Sex",y="Age",data=fd)


# In[14]:


##Facetgrid
f=sns.FacetGrid(fd,col="Survived")
f.map(plt.hist,"Age")

