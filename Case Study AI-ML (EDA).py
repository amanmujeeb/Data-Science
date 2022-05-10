#!/usr/bin/env python
# coding: utf-8

# In[1]:



#importing necessary packages to perform univariative and multivariative analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings


# In[2]:


#reading the csv
cgfdata = pd.read_csv("CardioGoodFitness.csv")


# In[3]:


#number of rows and columns
cgfdata.shape


# In[4]:


cgfdata.describe()


# In[7]:


#First ten rows of the data set
cgfdata.head(10)


# In[39]:


#Count of products
cgfdata['Product'].value_counts()


# In[41]:


#Count of Marital Status
cgfdata['MaritalStatus'].value_counts()


# In[43]:


#the type of data
cgfdata.dtypes


# In[44]:


#shows the value of each plot against each variablw
sns.pairplot(cgfdata, diag_kind="kde")


# In[52]:


#Converting Product to category
cgfdata.Product = cgfdata.Product.astype('category')


# In[53]:


cgfdata.dtypes


# In[54]:


#Univariative analysis, (products purchased)
sns.countplot(x="Product",  data=cgfdata)


# In[55]:


#Univariative analyis for porducts purchased by gender
sns.countplot(x="Gender",  data=cgfdata)


# In[56]:


#Distribution of Age of Users
sns.displot(cgfdata['Age'])


# In[57]:


#BOX Plot for Age 
sns.boxplot(x="Age", data=cgfdata)


# In[ ]:





# In[65]:


#Bivariative Analysis (Age) This shows us the dirstributionn of the population varys between the 25-35 age group
sns.boxplot(x="Age", y="Gender", data=cgfdata)


# In[68]:


#This boxplot helps us understand the everage miles covered by each specific gender
sns.boxplot(x="Miles", y="Gender", data=cgfdata)


# In[77]:


sns.catplot(x = 'Fitness', data = cgfdata, kind ='count');


# In[12]:


#this shows us that the TM195 is the most popular amomng the users followed by TM498 annd TM798
sns.catplot(x = 'Product', data = cgfdata, kind = 'count');


# In[62]:


#Distribution of Miles (Univariative Analysis)
sns.displot(cgfdata['Miles']);


# In[76]:


#this plot depicts the particular age group of people whihc mainly range between 25-30 use this product and these products are popular amongst the male population than the female/
sns.boxplot(x="Age", y="Product", data=cgfdata, hue = "Gender")


# In[63]:


correlation = cgfdata.corr()
correlation


# In[72]:


#looking at the heatmap we can infer that miles and fitness are closely related and income and education are also closely related. We also see that the relation between usage and fitness is comparitively high
sns.heatmap(correlation, annot=True)


# In[73]:


#depecits the relationship of each column vs the other in order to analyze and understand the data
sns.pairplot(cgfdata, kind = 'reg')
plt.show()


# In[81]:


#plot depicts the product usage displaying how popular the product is based on marital status
sns.barplot(x="Product", y="Usage",data=cgfdata, hue = "MaritalStatus")


# In[6]:


#Shows us the level of fitness and its relation to the product
sns.countplot(cgfdata.Fitness, hue=cgfdata.Product)


# In[9]:


#countplot to depict the usage varied with the products available
sns.countplot(cgfdata.Usage, hue=cgfdata.Product)


# In[10]:


sns.barplot(x="Fitness", y="Miles",data=cgfdata, hue = "Gender")


# In[11]:


sns.barplot(x="Fitness", y="Miles",data=cgfdata, hue = "Product")


# In[ ]:


#I would suggest that TM195 is the most popular among the age group of 25-35, so targeting and promoting the product in the older population is important
#TM798 needs to be narketed more compared to others as its the least so sold so new leads need to be generated
#The data shows that the fittest people cover tge mist mukes and the most popular equipment amongst the fit people is TM798 yet this product is not sold the most, so in order to promote more fitness, the TM798 needs to be marketed more
#The graph with pairplots depicts that there is a positive relation between fitness and usage and fitness and miles covered
#The heatmap provides us with key insights about how each variable relates to the other

