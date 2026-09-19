################################################
### Multiple Linear regression #################
#### SAT DATA Example ##########################
datasat = read.table("CASE1201.ASC.txt", header = TRUE)
attach(datasat)

## Fit full model
regression.line = lm(sat ~log(takers)  + rank + income + years + public + expend)
summary(regression.line)
## Compare to the model with confounding variables only
regression.red = lm(sat ~ log(takers) + rank)
anova(regression.red, regression.line)

## Obtain Mallow's Cp, AIC, BIC criterion values
library(CombMSC)
n = nrow(datasat)
## full model
c(Cp(regression.line,S2=24.86), AIC(regression.line,k=2),AIC(regression.line,k=log(n)))
## reduced model
c(Cp(regression.red,S2=24.86), AIC(regression.red,k=2),AIC(regression.red,k=log(n)))
library(boot)
## CV: 10-fold and leave one out 
gregression.line = glm(sat ~log(takers)  + rank + income + years + public + expend)
c(cv.glm(datasat,gregression.line,K=10)$delta[1], cv.glm(datasat,gregression.line,K=n)$delta[1])
gregression.red = glm(sat ~log(takers)  + rank)
c(cv.glm(datasat,gregression.red,K=10)$delta[1], cv.glm(datasat,gregression.red,K=n)$delta[1])

### Search over all  (2^6=64 models total)
library(leaps)
out = leaps(datasat[,-c(1,2)], sat, method = "Cp")
cbind(as.matrix(out$which),out$Cp)
best.model = which(out$Cp==min(out$Cp))
cbind(as.matrix(out$which),out$Cp)[best.model,]

### Apply Stepwise Regression

# Forward
step(lm(sat~log(takers)+rank), scope = list(lower=sat~log(takers)+rank,
     upper = sat~log(takers)+rank+expend+years+income+public), direction = "forward")

par(mfrow = c(1,1))
AIC = c(346.7, 331.66, 323.9)
ommitted = c(325.85, 327.8)
plot(1:3, AIC, xlim = c(1,5), type = "l", xaxt = "n", xlab = " ", main = "Forward Stepwise AIC Plot")
points(1:3, AIC, pch = 19)
points(4:5, ommitted)
axis(1, at = 1:5, labels = c("log(takers)+rank", "expend", "years", "income", "public"))
abline(h = 323.9, lty = 2)

# Backward
full = lm(sat~log(takers)+rank+expend+years+income+public)
minimum = lm(sat~log(takers)+rank)
step(full, scope = list(lower=minimum, upper = full), direction = "backward")

# Both
step(minimum, scope = list(lower=minimum, upper = full), direction = "both")
step(full, scope = list(lower=minimum, upper = full), direction = "both")

##### Ridge Regression ######################

library(MASS)
ltakers = log(takers)
predictors = cbind(ltakers, rank, income, years, public, expend)
predictors = scale(predictors)
sat.scaled = scale(sat)

lambda = seq(0, 10, by=0.25)
out = lm.ridge(sat.scaled~predictors, lambda = lambda)
round(out$GCV, 5)
which(out$GCV == min(out$GCV))

dim(out$coef)
round(out$coef[,10], 4)

regression.scale = lm(sat ~predictors)

par(mfrow = c(1,1))
plot(lambda, out$coef[1,], type = "l", col = 1, lwd=3, xlab = "Lambda", ylab = "Coefficients",
main = "Plot of Regression Coefficients vs. Lambda Penalty Ridge Regression", ylim = c(min(out$coef), max(out$coef)))
abline(h = 0, lty = 2, lwd = 3)
abline(v = 2.25, lty = 2,lwd=3)
for(i in 2:6)
points(lambda, out$coef[i,], type = "l", col = i,lwd=3)

##### Lasso Regression ######################

library(lars)
object = lars(x = predictors, y = sat.scaled)
plot(object)
object$Cp

plot.lars(object, xvar="df", plottype="Cp")

## Apply Lasso /Elastic Net
library(glmnet)

## alpha = 1 for lasso
Xpred= cbind(ltakers, rank, income, years, public, expend)
# Find the optimal lambda using 10-fold CV 
satmodel.cv=cv.glmnet(Xpred,sat,alpha=1,nfolds=10)
## Fit lasso model with 100 values for lambda
satmodel = glmnet(Xpred, sat, alpha = 1, nlambda = 100)
## Extract coefficients at optimal lambda
coef(satmodel,s=satmodel.cv$lambda.min)
## Plot coefficient paths
plot(satmodel,xvar="lambda",lwd=2)
abline(v=log(satmodel.cv$lambda.min),col='black',lty = 2,lwd=2)

## alpha = 0.5 (or other values different from 0,1) for elastic net
Xpred= cbind(ltakers, rank, income, years, public, expend)
# Find the optimal lambda using 10-fold CV 
satmodel.cv=cv.glmnet(Xpred,sat,alpha=0.5,nfolds=10)
## Fit lasso model with 100 values for lambda
satmodel = glmnet(Xpred, sat, alpha = 0.5, nlambda = 100)
## Extract coefficients at optimal lambda
coef(satmodel,s=satmodel.cv$lambda.min)
## Plot coefficient paths
plot(satmodel,xvar="lambda",lwd=2)
abline(v=log(satmodel.cv$lambda.min),col='black',lty = 2,lwd=2)



