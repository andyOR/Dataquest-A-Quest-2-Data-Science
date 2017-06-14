## In this script of guided project, we concepts of exploratory data analysis
## We will use dataset on the job outcomes of students who graduated from college between 2010 and 2012
## The original data on job outcomes was released by American Community Survey, which conducts surveys and aggregates the data.
## FiveThirtyEight cleaned the dataset and released it here https://github.com/fivethirtyeight/data/blob/master/college-majors/recent-grads.csv


## Introduction

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline # plots are displayed inline
recent_grads = pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]

recent_grads.head()
recent_grads.tail()

raw_data_count = recent_grads.shape[0]# number of rows
recent_grads = recent_grads.dropna() #dropping row with missing values

recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(7,10))# scatter plot

recent_grads['Median'].hist(bins=15, range=(0,120000))# histogram
plt.title("Distribution of Median Salary")
plt.xlabel("Median")
plt.ylim(0,80)
plt.ylabel("count")
