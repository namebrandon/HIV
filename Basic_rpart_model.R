#build formula
formula = "Resp ~ VL.t0 + CD4.t0 + PR.A + PR.B + PR.C + PR.D + PR.E + PR.F + PR.G + PR.H + PR.I + PR.K + PR.L + PR.M + PR.N + PR.P + PR.Q + PR.S + PR.T + PR.V + PR.W + PR.X + PR.Y + PR.Z + RT.A + RT.B + RT.C + RT.D + RT.E + RT.F + RT.G + RT.H + RT.I + RT.K + RT.L + RT.M + RT.N + RT.P + RT.Q + RT.S + RT.T + RT.V + RT.W + RT.X + RT.Y + RT.Z"

#you may need to do install.packages('rpart') if you have never installed the package before.
library('rpart')

#fit model
fit <- rpart(formula, data=train)

#create prediction based on model (note: must use type="class" for classification, otherwise
#you will get a vector of probabilities)

prediction <- predict(fit, test, type="Class")

#write results of prediction to CSV for comparison with actual results
submit <- data.frame(PatientID = test$PatientID, Resp=prediction)
write.csv(submit, file="results_for_comparison_rpart.csv", row.names=F)
