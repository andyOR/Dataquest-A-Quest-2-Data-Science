## Introduction To Functions

add <- function(a, b){
  d <- a + b
  return(d)
}


## Calling Functions

# Define the add function
add <- function(a, b){
  return(a + b)
}

# Call the add function with the arguments 1 and 2
print(add(1, 2))
d <- add(5,10)


## Defining A Function

# Enter your code here
subtract <- function(a,b) {
  p = a-b
  return(p)
}

d <- subtract(50,10)


## Reading In The Data

ufos <- read.csv("ufo_sightings.csv")


## Previewing The Dataframe With Head And Tail

# Print the first five rows in the dataframe
print(head(ufos, 5))
print(tail(ufos, 5))


## Calculating UFO Sightings Per Year

# Enter your code here
print(str(ufos))  


## Converting A Vector's Type

dateReported <- as.character(ufos$date.reported)
dateSighted <- as.character(ufos$date.sighted)


## Extracting Part Of A Character With The Substring Function

# This extracts "2004" from our string
date <- "20040415"
print(substr(date, 1, 4))

# This extracts the year from each string in the vector
dates <- c("20040415", "20080515")
print(substr(dates, 1, 4))

years <- substr(dateSighted, 1, 4)


## Generating A Table Of Sightings Per Year

# Create a small vector containing a few years
selectedYears <- c("2004", "2002", "1992", "2005", "2006", "2005", "2004")

# Create and print a table
print(table(selectedYears))

tab_years <- table(years)
print(tab_years)


## Working With Dates

dateSighted <- as.character(ufos$date.sighted)
dateSighted <- as.Date(dateSighted, "%Y%m%d")

dateReported <- as.character(ufos$date.reported)
dateReported <- as.Date(dateReported, "%Y%m%d")


## Subtracting Vectors

# Enter your code here
delay = dateReported - dateSighted


## Making A Table Of Reporting Delays

# Enter your code here
print(table(delay))


## Cleaning And Combining The Data

# Enter your code here
dates <- data.frame(dateReported, dateSighted)


## Introduction To Boolean Vectors

a <- c(1,2,3)
b <- c(5,2,5)

# Find when each element in a is greater than the corresponding element in b
print(a > b)

positiveDelays <- delay > 0


## Filtering With Boolean Vectors

filter <- c(FALSE, FALSE, TRUE, TRUE)
bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
twoFlavors <- bestIceCreamFlavors[filter,]
print(twoFlavors)

positiveDates <- dates[positiveDelays,]


## Removing Null Values

# Enter your code here
positiveDates <- dates[positiveDelays,]
cleanDates <- na.omit(positiveDates)


## Remaking Our Table

# Enter your code here

delay <- cleanDates$dateReported - cleanDates$dateSighted
print(delay)


## END