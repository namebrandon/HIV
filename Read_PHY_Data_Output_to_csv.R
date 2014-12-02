require(Biostrings)
require(seqinr)

setwd("/Users/brandon/Dropbox/Kaggle/HIV/Nov24")

virusaln  <- read.alignment(file = "training_data.phy", format = "phylip")
test_matrix <- as.matrix(virusaln)

install.packages("reshape2")
library(reshape2)

aligned_df <- as.data.frame(test_matrix)
write.csv(aligned_df, file="aligned_pr_sequences.csv")
