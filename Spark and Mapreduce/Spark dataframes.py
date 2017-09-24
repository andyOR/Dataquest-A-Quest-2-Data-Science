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


## Pandas vs. Spark Dataframes

df.show()


## Row objects

first_five = df.head(5)
for r in first_five:
    print(r.age)


## Selecting columns

df[['age']].show()
df[['age', 'males', 'females']].show()


## Filtering rows

five_plus = df[df['age']>5]
five_plus.show()


## Filtering columns

first_row = df[df['females']< df['males']]
first_row.show(20)


## Converting Spark dataframes to Pandas dataframes

pandas_df = df.toPandas()
pandas_df['total'].hist()

## END
