# This is basics of python

## assigning variables with values
china = 123
india = 124
united_states = 134
print(china)

## Display Values Using The Print Function
china = 123
print(china)
india = 124
print(india)
united_states = 134
print(united_states)

## Different Data types in Python
china_name = "China" # string data type
china_rounded = 123 # integer data type
china_exact = 122.5 # float data type
print(china_name)
print(china_rounded)
print(china_exact)

## finding the variable data type using "type" function
china_name = "China"
china_exact = 122.5
print(type(china_exact))

## converting data types in pyhton
china_rounded = 123
int_to_str = str(china_rounded)
str_to_int = int(int_to_str)

# commenting with hash function

# Neighbour Country
china = 123
# Home Country
india = 124
# Resident Country
united_states = 134

#Arithmetic Operations in python
china_plus_10 = china + 10
us_times_100 = united_states * 100
print(china_plus_10 + us_times_100)

# Order of operation in python is followed through PEMDAS sequence
#Parentheses -> Exponents -> Multiplcation -> Division -> Addition -> Subtraction
china = 123
india = 124
united_states = 134
china_celsius = (china - 32) * 0.56
india_celsius = (india - 32) * 0.56
us_celsius = (united_states - 32) * 0.56

## Using A List To Store Multiple Values. We use append feature t0 add values in list
countries = []
temperatures = []
countries.append("China")
countries.append("India")
countries.append("United States")
temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)
print(countries)
print(temperatures)

## Creating list with values directly as against append feature
temps = []
temps = ["China", 122.5, "India", 124.0, "United States", 134.1]

## Accessing Elements in a list
countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)


china = countries[0]
china_temperature = temperatures[0]

## Finding the length of the list using len() function
countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
two_sum = len(countries) + len(temperatures)

## Extraction of variable using slicing of lists
countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
countries_slice = countries[1:4]
end = len(temperatures)
temperatures_slice = temperatures[3:end]

##  END
