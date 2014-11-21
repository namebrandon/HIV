
# coding: utf-8

# In[102]:

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


# In[103]:

#Load the competition test data set into the 'df' variable as an example
#Note - Modify your path as appropriate

#Windows Path
train_converted = pd.read_csv("C:\\Users\\Brandon\\Documents\\IPython Notebooks\\HIV\\train_converted_na_removed.csv")
standard_seq = pd.read_csv("C:\\Users\\Brandon\\Documents\\IPython Notebooks\\HIV\\Standard_Gene_Sequence.csv")
#OSX Path
#df = pd.read_csv("/Users/brandon/Dropbox/Kaggle/HIV/training_data.csv")

#create new difference column, give it weird value to make sure it is properly populated
train_converted['PR_SEQ_DIFF_FROM_STANDARD'] = Decimal(9.99999)


# In[104]:

#initialize standard_sequence as empty
standard_sequence = ""

#loop through standard sequence codon groups and build string (pr.1-pr.99)
for i in range(1,100):
    column = "PR.Seq_"+str(i)
    standard_sequence = standard_sequence + standard_seq[column][0]


#for every row in our training set
for index,row in train_converted.iterrows():     
    
    #initialize each patient sequence as empty
    patient_sequence = ""
    
    #loop through pr.1-pr.99 columns for each patient and build a string
    for i in range(1,100):
        column = "PR.Seq_"+str(i)
        patient_sequence = patient_sequence + str(row[column])


#    print patient_sequence
#    print standard_sequence

    #initialize counter variables as 0
    difference_count =0
    total_count = 0
    same_count = 0
    percent_different = Decimal(0.000)

    #zip merges the two strings into a aligned set of tuples between each string (truncates to the smallest string!)
    u=zip(patient_sequence,standard_sequence)

    #compare each letter in the zip object
    for i,j in u:
        #if same letter increment same counter
        if i==j:
            same_count=same_count+1
            #print i,'--',j
        #if diff letter, increment different counter
        else:
            difference_count=difference_count+1
            #print i,'**',j
    
    total_count = Decimal(same_count) + Decimal(difference_count)
    #print total_count
    #print difference_count
    
    #calculate % different from standard
    percent_different = Decimal((difference_count) / total_count)
    
    #populate new column with % diff value
    train_converted.loc[index,'PR_SEQ_DIFF_FROM_STANDARD']=percent_different




# In[105]:

train_converted.to_csv("C:\\Users\\Brandon\\Documents\\IPython Notebooks\\HIV\\train_converted_na_removed_difference.csv")


# In[ ]:

7 columns
In [ ]:

