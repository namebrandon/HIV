
# coding: utf-8

# In[191]:

#import some standard libraries

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sklearn import datasets, svm



# In[192]:

#Load the competition test data set into the 'df' variable as an example
#Note - Modify your path as appropriate

df = pd.read_csv("E:\\Dropbox\\Kaggle\\HIV\\training_data.csv")


# In[193]:

#define our valid list of amino acids
amino_acid_letters =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']


# In[194]:

#create a PR new column for every letter in our amino acid list ie, PR_A, PR_B, etc..
for letter in amino_acid_letters:
    pr_letter = "PR_"+letter
    df[pr_letter] = float(0.00)

#create a RT new column for every letter in our amino acid list
for letter in amino_acid_letters:
    pr_letter = "RT_"+letter
    df[pr_letter] = float(0.00)


# In[195]:

#keeping for reference.. allows us to check the count for any given single record

#get PR SEQ COLUMN for 1st row
#s = df.ix[0,2] #specified as row #, col # where 0 is first row, 2 is 2nd column

#iterate through our list of amino acids
#for letter in amino_acid_letters:
    
#    count = s.count(letter)  #get frequency of each letter
#    length = s.__len__() #get length of sequence
#    percent = float(count)/ float (length) * 100 #get percentage of letter out of entire sequence
#    print letter+" "+str(count)+" "+'{0:.4f}'.format(percent)  #print



# In[196]:



for index, row in df.iterrows():                                         # iterate through every row in our data frame
    s = str(row['PR Seq'])                                               # load the PR sequence into string s
    length = s.__len__()                                                 # get length of sequence
    for letter in amino_acid_letters:                                    # iterate through amino acid list
        
        pr_letter = "PR_"+letter                                         # PR_ + A, PR_ + C, etc..
        
        count = s.count(letter)                                          #get frequency of each letter
        
        percent = float(count)/ float (length) * 100                     # get percentage of letter out of entire sequence
        
        df.loc[index, pr_letter]=percent                                 # save our percentage in appropriate column
        
        #print letter+" "+str(count)+" "+'{0:.2f}'.format(percent)       # debug statement / commented out

    


# In[197]:

# repeat the above cell, this time for RT Sequences

for index, row in df.iterrows():
    s = str(row['RT Seq'])
    length = s.__len__() 
    for letter in amino_acid_letters:
        
        rt_letter = "RT_"+letter
        
        count = s.count(letter)  
        
        percent = float(count)/ float (length) * 100 
        
        
        df.loc[index, rt_letter]=percent
        
        #print letter+" "+str(count)+" "+'{0:.2f}'.format(percent) 

  


# In[198]:

# write output
df.to_csv("E:\\Dropbox\\Kaggle\\HIV\\new_acid_columns.csv")


# In[198]:



