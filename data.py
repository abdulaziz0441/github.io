#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


import pandas as pd
from scipy import stats
import numpy as np
import seaborn as sns 
data = pd.read_csv("es.csv")
cm = sns.light_palette("red", as_cmap=True)
data.style.background_gradient(cmap=cm)


# In[4]:


colum = data.columns.tolist()
for x in colum:
    ds=[x for x in data[x]]
    desc= data[x].describe()
    array= [x for x in desc]
    print("Detail kolom ",x)
    print("rata-rata: ",array[1])
    print("Median: ",np.median(np.array(ds)))
    print("Modus: ", stats.mode(ds))
    print("Standard deviasi: ",np.std(ds))
    print("varian: ", stats.variation(ds))
    print("Skewness: ",stats.skew(ds))
    print("Quartil 1: ",array[4])
    print("Quartil 2: ",array[5])
    
    print("\n")


# In[ ]:




