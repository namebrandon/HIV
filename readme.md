#UChicago HIV - Example Models

##Data
There are two files for use with building the models. These are based on the original training .csv being run through Adam's .R script. Additionally they contain my letter freqency counts in new columns. If you wish to delete those new columns and use a pure train/test set, please feel free. 

* train_freq_columns.csv   

* test_freq_columns.csv   

##Building models in R
Once you have these files, the following R files will allow you to build a model. Please read through the model building examples and look at the help documentation for rpart() and randomForest(). There are additional paramters you can try and tweak, and see if you can improve the score(s).

* File_Preprocessing.R - This imports the data and does some housecleaning.

* Basic_rpart_mode.R - This creates a basic classification tree and saves the output to a .csv file.

* Basic_RandomForest_model.R - This creates a basic RF model and saves the output to a .csv file.

##Scoring (Excel)
Once you have the output .csv file from your model, you can score your results.

* model_results.xlsx 
 
The Excel workbook has two sets of two columns. One of those sets you should overwrite with your result data (from the output .csv files). The other columns contain the correct results. When you paste your model's results into the .XLSX, it will give you a percentage correct.

