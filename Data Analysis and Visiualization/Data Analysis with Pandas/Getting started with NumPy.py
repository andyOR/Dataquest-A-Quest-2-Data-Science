# In this script, we will be using "world_alcohol.csv" file which contains data consumption of alcohol per capita in different countries

## The dataset contains five columns representing year of data (Year), region in which the country is located (WHO), country,
##type of alcohol consumed (Beverage types), and avergage number of liters alcohol consumed (Display Value)

## Getting data ready for analysis. Creatng list of lists with no header column
import csv

O = open("world_alcohol.csv", 'r')
alcohol_data = csv.reader(O)
world_alcohol = list(alcohol_data)

world_alcohol = world_alcohol[1:]

## Performing addition and avergae function on year column
years = []

for row in world_alcohol:
    y = row[0]
    years.append(y)
    
total = 0
for row in years:
    total = total + float(row)
    
avg_year = total/(len(years))

## Introducing NumPy. NumPy is a python module that is used to create and manipulate multidimensional arrays
## Using NumPy

import numpy # need to import numpy first
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter = ",")# dataset is read using "numpy.genformtxt()" function. This will read dataset into numpy.ndarray class

print(type(world_alcohol))

## Creating arrays. Arrays can be created in NumPy using "numpy.array()" function

vector  = numpy.array([10, 20, 30]) #one dimensional array

matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]]) # two dimensional array often used for list of lists

## Array shape. function "ndarray.shape()" will help us to find the property of matrices like rows and columns
#Note: shape property output tuple with number of elements. A tuple is a list where elements can't be altered

vector = numpy.array([10, 20, 30])
vector_shape = vector.shape

matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
matrix_shape = matrix.shape

## Data types in NumPy. Some of the data types in NumPy are boolen, integers, float, etc. Type of data can be checked using "dtype"

world_alcohol_dtype = world_alcohol.dtype

##All the values in NumPy has to be of the same data type. NumPy will convert all the diiferent data type into same data type

##Reading the data properly. We can use different set properties in numpy.genfrmtxt() to read data with different data types
# dtype U75 for data type, skip_header to skip header row
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter = ",", dtype = "U75", skip_header = 1)
print(world_alcohol)

##Indexing arrays

uruguay_other_1986 = world_alcohol[1,4] # for extracting amount of alcohol consumed in uruguay
third_country = world_alcohol[2,2] #extracting country from row 3

## Slicing arrays. it has four forms to slice lists
countries = world_alcohol[:,2]# extracting entire third column
alcohol_consumption = world_alcohol[:,4] # etracting fourth column

## Slicing one dimension
first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,:]

#Slicing arrays
first_twenty_regions = world_alcohol[0:20, 1:3]

##End
