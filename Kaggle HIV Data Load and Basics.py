
# coding: utf-8

# In[4]:

#import some standard libraries

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sklearn import datasets, svm


# In[29]:

#Load the competition test data set into the 'df' variable as an example
#Note - Modify your path as appropriate

df = pd.read_csv("/home/brandon/Kaggle_HIV/test_data.csv")


# In[7]:

#top 10 records in dataframe
df.head(10)



# In[30]:

#only records where CD4-t0 > 700
df[df['CD4-t0'] > 700]


# In[23]:

# only records where CD4-t0 > 700 AND VL-t0 >2.00

df[(df['CD4-t0'] > 700) & (df['VL-t0'] > 2.00)]


# In[24]:

#get the mean of the CD4-t0 column
df['CD4-t0'].mean()


# In[26]:

#create subset based on example above and store in a new variable
subset_results = df[(df['CD4-t0'] > 700) & (df['VL-t0'] > 2.00)]


# In[28]:

#write subset results to .csv file
subset_results.to_csv("/home/brandon/Kaggle_HIV/output_example_data.csv")


# In[ ]:



