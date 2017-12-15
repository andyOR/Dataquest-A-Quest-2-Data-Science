## In this script, we will learn R-programming fundamentals


## Performing multiple calculations

print(84+95+79)/3
print(95+86+93)/3


## Performing arithmetic calculation

print(77+ 85+ 90)/3

print(92+ 90+ 91)/3

print(85+ 88+ 95)/3


## Performing Calculations with Order of Operations

88 - ((88+87.66667+86+91.33333+84+91+89.33333)/7)


## Creating comments


print(
    88 - ((88 + 87.66667 + 86 + 91.33333 + 84 + 91 + 89.33333)/7) #math score devaition from average
)


## Assigning values for variables

math <- 88 

# Add your code below

chemistry<- 87.66667
writing<- 86
art<-91.33333
history<- 84
music<- 91
physical_education<- 89.33333


## performing calculation using variables

math <- 88 
chemistry <- 87.66667
writing <-  86
art <- 91.33333
history <- 84
music <- 91
physical_education <- 89.33333

gpa = (math + chemistry + writing + art + history + music + physical_education)/7

history_difference <- history - gpa


## Creating vectors

math <- 88 
chemistry <- 87.66667
writing <-  86
art <- 91.33333
history <- 84
music <- 91
physical_education <- 89.33333

final_scores = c(math,chemistry,writing,art,history,music,physical_education)


## Performing operations on vectors


final_scores <- c(math, chemistry, writing, art, history, music, physical_education)

highest_score <- max(final_scores)
lowest_score <- min(final_scores)
num_classes <- length(final_scores)


## END





















