library('randomForest')
fit.rf <- randomForest(Resp ~ VL.t0 + CD4.t0 + PR.A + PR.B + PR.C + PR.D + PR.E + PR.F + PR.G
                       + PR.H + PR.I + PR.K + PR.L + PR.M + PR.N + PR.P + PR.Q + PR.S + PR.T
                       + PR.V + PR.W + PR.X + PR.Y + PR.Z + RT.A + RT.B + RT.C + RT.D + RT.E
                       + RT.F + RT.G + RT.H + RT.I + RT.K + RT.L + RT.M + RT.N + RT.P + RT.Q
                       + RT.S + RT.T + RT.V + RT.W + RT.X + RT.Y + RT.Z 
                       ,nodesize=3, ntree=25000
                       ,data=train)
predict.rf <- predict(fit.rf, test)
submit.rf <- data.frame(PatientID = test$PatientID, Resp=predict.rf)
write.csv(submit.rf, file="results_for_comparison_rf.csv", row.names=F)
