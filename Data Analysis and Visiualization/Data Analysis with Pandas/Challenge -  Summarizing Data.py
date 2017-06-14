## In this script, we will be working on a challenge to apply all the previous learnings
## we had from the data visualization in dataquest

## Introduction To The Data.

# we will be working with two dataset, one from all ages group employment data "all-ages.csv"
# and second with recent grads from majors. "recent-grads.csv"


## Introduction To The Data

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])


## Summarizing Major Categories

# Unique values in Major_category column and number of members in each dataset
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()# dictionary assignement in pandas

unique_category1 = all_ages['Major_category'].unique()
unique_category2 = recent_grads['Major_category'].unique()

for row in unique_category1:
    row_category = all_ages[all_ages["Major_category"] == row]
    row_total = row_category["Total"]
    row_sum = row_total.sum()
    aa_cat_counts[row] = row_sum
    

for row in unique_category2:
    row_category = recent_grads[recent_grads["Major_category"] == row]
    row_total = row_category["Total"]
    row_sum = row_total.sum()
    rg_cat_counts[row] = row_sum


## Low-Wage Job Rates

import numpy as np
low_wage_percent = 0.0



low_wage_percent = (recent_grads["Low_wage_jobs"].sum() / (recent_grads["Total"].sum()))


## Comparing Data Sets

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for row in majors:
    row_class_grads = recent_grads[recent_grads["Major"] == row]
    row_class_ages = all_ages[all_ages["Major"] == row]
    
    row_grads_un = row_class_grads["Unemployment_rate"].values[0]
    row_ages_un = row_class_ages["Unemployment_rate"].values[0]
    
    if row_grads_un < row_ages_un:
        rg_lower_count +=1



##  End
