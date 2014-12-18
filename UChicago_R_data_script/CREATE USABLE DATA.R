# Import the data - MAKE SURE THE DATA IS IN THE WORKING DIRECTORY !!
data = read.csv('training_data HIV.csv')
# using summary we see var 1 is just the patient # which is just the row # and var 2 is Resp

# since we want to having training data with the correct proportion of good and bad response,
# I first separate out the two responses-
good = subset(data,data$Resp==1)
bad = subset(data,data$Resp ==0)

# using either length or 'global environment in R Studio we see len(bad)= 794 and len(good) = 206
# I couldn't get the caret fn createDataPartition to work, presumably because the gene lenghts threw
#it off somehow.  No worries- use sample 

#use 85% of the data - later we can decide if we want 70% train, 15% validate or what
samp1 = sample(206,.85*206) # create a random subset of our index of the right length
samp1 = sort(samp1) # order it
samp0 = sample(794, .85*794)
samp0 = sort(samp0)
# partition our data
train1 = good[samp1,]
train0 = bad[samp0,]
train = rbind(train0,train1)

# We need to save the testing data - it's a little kludgy, but this works-
m0 = matrix(1:794)
tst0 = subset(m0,!(m0 %in% samp0))
m1 = matrix(1:206)
tst1 = subset(m1, !(m1 %in% samp1))
test0 = bad[tst0,]
test1 =good[tst1,]
test = rbind(test0,test1) ; write.csv(test,'test.csv')
train = rbind(train0,train1);  write.csv(train,'train.csv')

dl = c('test0','test1','train0','train1','tst0','tst1')
rm(list = dl)
dl = c('m0','m1','samp0','samp1','good','bad')
rm(list = dl); rm(dl)

