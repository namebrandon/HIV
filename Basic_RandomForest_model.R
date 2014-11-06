#set working direction - CHANGE THIS FOR YOUR LOCATIONS!!
setwd("E:/your_path_here/")

#load random forest library (again you may need to do install.packages('randomForest')
#if you have never installed the library before.

library('randomForest')

#fit our model
# - For some reason using the formula variable causes an error, so I just hard-coded this formula

fit.rf <- randomForest(Resp ~ VL.t0 + CD4.t0 + PR.A + PR.B + PR.C + PR.D + PR.E + PR.F + PR.G
                       + PR.H + PR.I + PR.K + PR.L + PR.M + PR.N + PR.P + PR.Q + PR.S + PR.T
                       + PR.V + PR.W + PR.X + PR.Y + PR.Z + RT.A + RT.B + RT.C + RT.D + RT.E
                       + RT.F + RT.G + RT.H + RT.I + RT.K + RT.L + RT.M + RT.N + RT.P + RT.Q
                       + RT.S + RT.T + RT.V + RT.W + RT.X + RT.Y + RT.Z 
                       ,nodesize=2, ntree=5000
                       ,data=train)

#create predictions based on model
predict.rf <- predict(fit.rf, test)

#create submit dataframe
submit.rf <- data.frame(PatientID = test$PatientID, Resp=predict.rf)

#write submit data_frame to file
write.csv(submit.rf, file="results_for_comparison_rf.csv", row.names=F)
