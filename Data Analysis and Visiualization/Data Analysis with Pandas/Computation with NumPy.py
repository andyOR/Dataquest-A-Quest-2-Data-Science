# In this script we will work with same world alcohol data we used in getting started
# with NumPy


## Array Comparison. This will compare values in t he dataset with given values.
## It will store them in another matrix with boolean results

countries_canada = world_alcohol[:,2] == "Canada"

years_1984 = world_alcohol[:,0] == "1984"

## Selecting elements. This will be used extract values where array comprison is positive

country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = world_alcohol[country_is_algeria,:]

# Comparison can ne done using multiple conditions as well using and "&" and or "|"
is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## Replacing values using array comparison

matrix = world_alcohol[:,0] == "1986"
world_alcohol[matrix,0] = "2014" # Replaced 1986 with 2014 in first column

matrix2 = world_alcohol[:,3] == "Wine"
world_alcohol[matrix2, 3] = "Grog"

## Replacing empty string " "
is_value_empty = world_alcohol[:,4] == ""
world_alcohol[is_value_empty, 4] = 0 # replacing empty string in 5th column with 0

## Converting data types using "astype()" function
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption.astype(float) # fifth column is replaced with float values from string

# Computing with NumPy.
total_alcohol = alcohol_consumption.sum() # sum computation on display value
average_alcohol = alcohol_consumption.mean()

## Total Annual alcohol consumption

canada1 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada")
canada_1986 = world_alcohol[canada1,4] 
canada_alcohol  = canada_1986.astype(float)

total_canadian_drinking = canada_alcohol.sum()

#Calculating consumption for each country

totals = {}

match_year = world_alcohol[:,0] == "1989"
year = world_alcohol[match_year, :]


def consume(country):
    country_consume = year[:, 2] == country
    country_consumption = year[country_consume,4]
    fifth_column = country_consumption == ""
    country_consumption[fifth_column] = 0
    w = country_consumption.astype(float)
    return w.sum()
    
    

for country in countries:
    totals[country] = consume(country)
    
print(totals)

## Finding The Country That Drinks The Most

highest_value = 0
highest_key = None

for country in totals:
    highest_count = totals[country] # this is value associated with the key
    if highest_count > highest_value:
        highest_value = highest_count
        highest_key = country # this is the key or country with highest consumption


##End        





