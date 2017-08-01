## In this script, we'll walk through the building blocks of making a decision tree automatically.


## Overview Of The Data Set

import pandas

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age)
income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))


## Converting Categorical Variables

# Convert a single column from text categories to numbers
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

for name in ["education", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "high_income"]:
    col = pandas.Categorical.from_array(income[name])
    income[name] = col.codes


## Splitting Data


## Creating Splits

