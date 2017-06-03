## In this script we will deal with missing data using Titanic dataset

## Introduction

import pandas as pd  ##using pd short form for pandas

titanic_survival = pd.read_csv("titanic_survival.csv")

## Finding The Missing Data

age = titanic_survival["age"]
print(age.loc[10:20])

age_null = pandas.isnull(age) # finding null values in column age
age_null_true = age[age_null]
age_null_count = len(age_null_true)
print(age_null_count)

## Whats The Big Deal With Missing Data? Missing data will obstruct operation with presence of NAN

age_is_null = pd.isnull(titanic_survival["age"])

age_not_null = titanic_survival["age"][age_is_null == False] # choosing values that are not NAN

correct_mean_age = sum(age_not_null) / len(age_not_null)

## Easier Ways To Do Math. ignoring NAN values using mean() function

correct_mean_age = titanic_survival["age"].mean()

correct_mean_fare = titanic_survival["fare"].mean()

## Calculating Summary Statistics

passenger_classes = [1, 2, 3]
fares_by_class = {}

for row in passenger_classes:
    row_class = titanic_survival[titanic_survival["pclass"] == row] # finding only rows where pclass is equal to "1,2 and 3"
    fare_m = row_class["fare"]
    fare_class = fare_m.mean()
    fares_by_class[row] = fare_class

## Making Pivot Tables. This function help us to subset rows by unique values in columns and calculate statitics on such columns

passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")

passenger_age = titanic_survival.pivot_table(index = "pclass", values = "age")
print(passenger_age)

## More Complex Pivot Tables. using more than one column to subset

import numpy as np

port_stats = titanic_survival.pivot_table(index = "embarked", values = ["fare", "survived"], aggfunc = np.sum)
print(port_stats)


## Drop Missing Values. dropna()


drop_na_rows = titanic_survival.dropna(axis=0)

drop_na_columns = titanic_survival.dropna(axis = 1)
new_titanic_survival = titanic_survival.dropna(axis = 0, subset = ["age", "sex"])


## Using Column Indexes

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row__index_83_age = new_titanic_survival.loc[83,"age"]
row_index_1000_pclass = new_titanic_survival.loc[766,"pclass"]

row_index_1100_age = new_titanic_survival.loc[1100, "age"] # using row index
row_index_25_survived = new_titanic_survival.loc[25, "survived"]
five_rows_three_cols = new_titanic_survival.iloc[0:5, 0:3] # in new dataset


##Reindexing Rows

titanic_reindexed = new_titanic_survival.reset_index(drop = True) # not retaining old index
print(titanic_reindexed.iloc[0:5,0:3])


## Apply Functions Over A DataFrame. we use function in pandas by dataframe.apply()

def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)

def null_col(function):
    null_columns = pd.isnull(function)
    null_length = function[null_columns == True]
    return len(null_length)

column_null_count = titanic_survival.apply(null_col)


## Applying A Function To A Row. using axis = 1, we can use function over row


def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)

def is_minorage(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"


## Calculating Survival Percentage By Age Group. using pivot to find the survival rate by age group

age_group_survival = titanic_survival.pivot_table(index = "age_labels", values = "survived", aggfunc = np.mean)


## END

















    


