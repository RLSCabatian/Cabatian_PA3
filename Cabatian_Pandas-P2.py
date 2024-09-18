#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[9]:


cars = pd.read_csv('cars.csv')
cars


# In[11]:


#Print data frame with odd-numbered columns that contains the first five rows
odd = cars.iloc[:5,::2]
odd


# In[13]:


#Print the row for the model "Mazda RW4 Wag
cars.loc[[1]] 


# In[15]:


#Print the cyl value for car model "Camaro Z28" 
cars.loc[[23],['cyl']]


# In[17]:


#Print the cyl and gear of the given model cars
cars.loc[[1,18,28],['Model','cyl','gear']] 


# In[ ]:




