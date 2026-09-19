
## Analysis of Singers' data

data = read.table("voice_and_height.txt",header=TRUE)

### sample sizes
n1 = length(data[(data[,1]!=0),1])
n2 = length(data[(data[,2]!=0),2])
n3 = length(data[(data[,3]!=0),3])
n4 = length(data[(data[,4]!=0),4])

# put the data into a vector and remove entries with zero's
data = as.vector(as.matrix(data))
missingv = which(data==0)
data = data[-missingv]

# create a vector that assigns each value to a pitch type
type = c(rep("Soprano",n1),rep("Alto",n2),rep("Tenor",n3),rep("Bass",n4))
# we need to transform vector type from numeric to factor
type = as.factor(type)

# visulize the height by picth
boxplot(data~type)

# apply ANOVA
pitch.aov = aov(data~type)

# Additional Analysis
## Diagnostic plots
plot(pitch.aov)

## More extensive output
 summary(pitch.aov)
 model.tables(pitch.aov,type = "means")
  
## Pairwise comparison
TukeyHSD(pitch.aov, conf.level = .95)

################################################################################

## Analysis of Carpet Data

# In order to read the data in a matrix I replaced * with 0
carpet.data = as.matrix(read.table("carpet_data.txt"))
# put the data into a vector and remove entries with zero's
carpet.data = as.vector(carpet.data)
missingv = c(1:length(carpet.data))[carpet.data==0]
carpet.data = carpet.data[-missingv]

# create a vector that assigns each value to a carpet type
type = c(rep(1,16),rep(2,16),rep(3,13),rep(4,16),rep(5,14),rep(6,15))
# the length of the type and carpet data should be equal to 90
print(length(carpet.data))
print(length(type))
# we need to transform vector type from numeric to factor
type = as.factor(type)

# visualize the carpet wear by type of carpet
boxplot(carpet.data~type, xlab="Type of carpet",ylab="Wear")

## ANOVA
carpet.aov = aov(carpet.data~type)

## Diagnostic plots
plot(carpet.aov)

resid.carpet = residuals(carpet.aov)


## More extensive output
 summary(carpet.aov)
 model.tables(carpet.aov,type = "means")
 
## Pairwise comparison
TukeyHSD(carpet.aov, conf.level = .95)


################################################################################

## Analysis of Keyboard Data

keyboard = as.matrix(read.table("keyboard_data.txt"))
keyboard = as.vector(keyboard)
keyboard = keyboard[-c(1:length(keyboard))[keyboard==0]]
length(keyboard)
layout = c(rep(1,12),rep(2,10),rep(3,11))
length(layout)
layout = as.factor(layout)

# visualize
boxplot(keyboard~layout, xlab="Keyboard layout",ylab = "Times taken to perform a task")

## ANOVA
keyboard.aov = aov(keyboard~layout)

## Diagnostic plots
plot(keyboard.aov)

## More extensive output
summary(keyboard.aov)
model.tables(keyboard.aov,type = "means")

TukeyHSD(keyboard.aov, conf.level = .95)
