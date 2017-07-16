## Introduction

# In the last mission, we looked at some R basics, including vectors. R stores most data as vectors.

# We'll explore vectors in greater depth in this mission, along with other ways to structure data


## Reading Data Into R

congress <- read.csv("114_congress.csv")

whiteHouse <- read.csv("2015_white_house.csv")


## Using Matrices To Store Multi-Dimensional Data


## Creating A Matrix

# Create a simple matrix with three rows and two columns
B <- matrix(c(1,2,3,4,5,6), 3, 2)
print(B)

C <- matrix(c("Rambo", "Chuck Norris", "Arnold", "Steven Seagal", "John Wayne", "Steve McQueen"),2,3)


## Using Indexes To Get A Matrix Element

# Print the first column of the second row
print(C[2,1])

# Print the third column of the second row
print(C[2,3])

c22 <- C[2,2]

c13 <- C[1,3]


## Using Indexes To Get Rows And Columns

# The first row of C
print(C[1,])

# The first column of C
print(C[,1])

c20 <- C[2,]

c03 <- C[,3]


## Understanding The Dataframe Data Type

# Get the salary column from the whitehouse data
salary <- whiteHouse["Salary"]

# Get the salary of the first employee in our data (from the salary column of the first row)
firstSalary <- whiteHouse[1,"Salary"]

whiteHouseNames <- whiteHouse["Name"]

status5 <- whiteHouse[5, "Status"]


## Finding The Average Salary With The Sum And Nrow Functions

# Enter your code here
Sumall <- sum(whiteHouse["Salary"])

lengthall <- nrow(whiteHouse)

averageSalary <- Sumall/lengthall


## Finding The Highest And Lowest Salaries With Min And Max

# Enter your code here

highestSalary <- max(whiteHouse["Salary"])

lowestSalary <- min(whiteHouse["Salary"])


## Indexing Method Results Have Subtle Differences

# Returns a dataframe
salaryFrame <- whiteHouse["Salary"]

# Returns a vector
salaryVector <- whiteHouse[,"Salary"]

whiteHouseNames <- whiteHouse["Name"]

whiteHouseNamesVector <- whiteHouse[, "Name"]


## 

# Find the index of the person with the lowest salary
# This is where knowing what kind of indexing returns what value comes in handy  
# We need a vector
minimumIndex <- which.min(whiteHouse[,"Salary"])
# Extract the row containing the lowest salary
minimumSalaryRow <- whiteHouse[minimumIndex,]
# Get the name column from that row
lowestEarner <- minimumSalaryRow["Name"]
# Print the name of the White House employee who earned the least
print(lowestEarner)

maximumIndex <- which.max(whiteHouse[,"Salary"])
# Extract the row containing the highest salary
maximumSalaryRow <- whiteHouse[maximumIndex,]
# Get the name column from that row
highestEarner <- maximumSalaryRow["Name"]
# Print the name of the White House employee who earned the highest
print(highestEarner)


## END