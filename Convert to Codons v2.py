
# coding: utf-8

# In[1]:

#import some standard libraries
      
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sklearn import datasets, svm
from patsy import dmatrices
import statsmodels.api as sm
from decimal import Decimal
get_ipython().magic(u'pylab inline')


# In[29]:

#Note - Modify your path as appropriate

#Windows Path
train_aligned = pd.read_csv('E:\\Dropbox\\Kaggle\\HIV\\Nov24\\training_data_aligned_full.csv')

#OSX Path
#train_aligned = pd.read_csv('/Users/brandon/Dropbox/Kaggle/HIV/Nov24/training_data_aligned_full.csv')


# In[30]:

#iterate through all rows
for index,row in train_aligned.iterrows():     
    #initialize each variable as empty
    codon = ""
    new_column_name = ""

  #create triple/codon columnns
    for i in range(1,298):
        column = "PR_"+str(i)
        codon = codon + str(train_aligned[column][index])
        if i % 3 == 0:
            new_column_name = "CODON_"+str(i)
            #print new_column_name + \: \ + codon
            train_aligned.loc[index,new_column_name]=codon
            #train_aligned[new_column_name][index]=codon
            codon = ""


# In[36]:

#drop individual columns
for i in range(1,298):
    column = "PR_"+str(i)
    train_aligned.drop(column, axis=1, inplace=True)


# In[37]:




# In[38]:

train_aligned.to_csv("E:\\Dropbox\\Kaggle\\HIV\\Nov24\\Full_Training_Aligned_PR_Codons.csv")


# In[ ]:



