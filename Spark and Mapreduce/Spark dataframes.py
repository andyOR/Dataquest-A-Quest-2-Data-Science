## The Spark DataFrame is a feature that allows you to create and work with DataFrame objects.

## For this mission, we'll be working with a JSON file containing data from the 2010 U.S. Census.

## Introduction

f = open('census_2010.json')

for i in range(0,4):
    print(f.readline())


## Reading in data

# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into a DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))


## Schema

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()


## 
