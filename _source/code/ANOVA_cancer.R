cancer_data<-read.table("CancerStudy.txt",header=T)
survival = cancer_data$Survival

## Explore the response variable
hist(survival,xlab=" ", ylab = "Number of Survival Days",main=" ",nclass=15)
hist(log(survival),xlab=" ", ylab = "Number of Survival Days",main=" ",nclass=15

## Need to specify Response & Categorical Variables
survival = log(survival)
cancertype = cancer_data$Organ
## Convert into cateogorical variable in R
cancertype = as.factor(cancertype)
boxplot(survival~cancertype, xlab = "Cancer Type", ylab = "Log(Number of Survival Days)")


## ANOVA in R
model = aov(survival~ cancertype)
summary(model)

## Estimated model parameters
model.tables(model,type = "means")


# Pairwise Comparison
TukeyHSD(anova_model)


par(mfrow=c(2,2))
qqnorm(residuals(model)) 
qqline(residuals(model))
hist(residuals(model),main="Histogram of residuals",xlab="Residuals")
plot(residuals(model),xlab="Order",ylab="Residuals")
abline(0,0,lty=1,col="red")
plot(fitted(model), residuals(model),xlab="Fitted values",ylab="Residuals")
abline(0,0,lty=1,col="red")



