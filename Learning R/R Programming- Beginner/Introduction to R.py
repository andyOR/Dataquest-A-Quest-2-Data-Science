## Overview Of The Data

# For this lesson, we'll be using a data set of White House employee salaries, which you can find at https://obamawhitehouse.archives.gov/briefing-room/disclosures/annual-records/2015


## Assigning A Value To A Variable

# This is a comment, and so is any line that starts with a #
# Comments provide helpful information about the code

# Assign the value 10 to the variable bearAwesomeness
bearAwesomeness <- 10

# Assign the value 1.5 to the variable guineaPigAwesomeness
guineaPigAwesomeness <- 1.5

dogAwesomeness <- 10
catAwesomeness <- 9.5


## Displaying Results With The Print Function

# We can print out values
print(10)

# We can also assign a value to a variable, then print the variable
lifeSavings <- 9999
print(lifeSavings)


## Numeric Vs. Character Variables

# Assign the value 800 to the variable runDistance
runDistance <- 800

# runDistance is of type "numeric"
print(class(runDistance))

# Assign the value "Peanut Butter Cup" to favoriteDessert
favoriteDessert <- "Peanut Butter Cup"

# favoriteDessert is of type "character" because it contains text
print(class(favoriteDessert))

biggestDog <- "Mastiff"
mastiffCount <- 50

biggestDogType <- class(biggestDog)
mastiffCountType <- class(mastiffCount)


## Storing Values As Vectors

# Store a vector of Russian presidents
russianPresidents <- c("Mikhail Gorbachev", "Boris Yeltsin", "Vladimir Putin")

# Store a vector of stock prices on consecutive days
applePrices <- c(113, 114, 115)

fibonacci <- c(0,1,1,2)


## Storing Single Values As Vectors

dogCount <- 1
catCount <- c(1)

# We can see that these two assignments are identical
# Both dogCount and catCount are vectors
print(identical(dogCount, catCount))


## Looking Up The Data In A Vector With Indexes

# Print the first element in salaries
print(salaries[1])

# Print the 50th element in salaries
print(salaries[50])

salary10 <- salaries[10]


## Finding A Vector's Length

# Initialize the runDistances vector
runDistances <- c(20, 10.5, 30)

# Print the length of the vector
print(length(runDistances))

# We've loaded in the salaries variable for you

salariesLength = length(salaries)


## Performing Math On Vectors

# Create a vector of stock prices
stockPrices <- c(10, 9, 11, 15)

# This creates a new vector.  Notice how every element has increased by two
# Every time you do math on a vector, it will change all the elements it contains
print(stockPrices + 2)

# stockPrices is unaffected, however
print(stockPrices)

lowerSalaries = salaries/3


## Using The Carrot To Overwrite Variables

# Initialize our list of stock prices again
stockPrices <- c(10, 9, 11, 15)

# Multiply every stock price by two, and overwrite the variable with the result
stockPrices <- stockPrices * 2
print(stockPrices)

salaries <- salaries - 5000


## Restrictions On Vector Types

mixedVector <- c("Fifteen", 15, 0)

# Everything in mixedVector is a character value
print(mixedVector)

# mixedVector is of type character
print(class(mixedVector))


## Using The Help Function To Get Help With R

help(class)# Enter your code here

## END


































