## In this script or course, we will uncover data visulaization techniques
## to explore datasets and relations among variables through charts
## We will be using US unemployment data


## Introduction to the data

# In this script, we will use monthly unemployment rate in US from 1948 till August 2016
# file "unrate.csv". We need to convert month column from text object to the datetime type using the pandas.to_datetime() function

import pandas as pd
df['col'] = pd.to_datetime(df['col'])


import pandas as pd

unrate = pd.read_csv("unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate.loc[0:12]


## Table Representation


## Observations From The Table Representation


## Visual Representation. Plots are a category of visual representations that allow us to easily understand the relationships between variables. For our dataset, we
## use line charts to compare the unemployment trends across time


## Introduction To Matplotlib. Matplotlib library helps to create line charts and plots. The pyplot module provides a high-level interface for matplotlib that
## allows us to quickly create common data plots and perform common tweaks to them

import matplotlib.pyplot as plt # to import matplotlib

plt.plot() # to generate plot
plt.show() # to show plot


## Adding Data. Instead of manually updating the ticks, drawing each marker, and connecting the markers with lines, matplotlib can handle the values if given as parameters

x_values = unrate[0:12]
y_values = unrate[0:12]

plt.plot(x_values["DATE"], y_values["VALUE"])
plt.show() # plotting first 12 data points


## Fixing Axis Ticks. In this, we will learn to fix x ticks characterisitcs using xticks() function

date = unrate["DATE"]
value = unrate["VALUE"]

plt.plot(date[0:12], value[0:12])
plt.xticks(rotation = 90)
plt.show()


## Adding Axis Labels And A Title

date = unrate["DATE"]
value = unrate["VALUE"]

plt.plot(date[0:12], value[0:12])
plt.xticks(rotation = 90)

plt.xlabel("Month") # xlabel added
plt.ylabel("Unemployment Rate")# ylabel added
plt.title("Monthly Unemployment Trends, 1948") # added title
plt.show()


## END

