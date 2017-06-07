## in this script, we will explore how to create multiple plots that are subsetted using one or more conditions
## We'll be working with the seaborn visualization library, which is built on top of matplotlib.
## Seaborn has good support for more complex plots, attractive default styles, and integrates well with the pandas library


## In this script, we will be using "Titanic shipwreck" dataset used in Kaggle leaning platform.


## Introduction to the Data
# There are two files in the data, one is train.csv and test.csv. It includes information on the
# passenger with columns Passenger Id, survived, etc.


import pandas as pd

titanic = pd.read_csv("train.csv")
titanic = titanic[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
titanic = titanic.dropna()
print(titanic.columns)


## Creating Histograms In Seaborn

import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot(titanic['Age'])
plt.show()


## Generating A Kernel Density Plot. we are only showing KDE smooth curve with area under the curve in color

sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel("Age")
plt.show()


## Modifying The Appearance Of The Plots.

import seaborn as sns
#sns.set_style("white")
#sns.kdeplot(titanic['Age'], shade=True)
#plt.xlabel("Age")
#sns.despine(left = True, bottom  = True)

sns.set_style('white') # white background with no grid
sns.kdeplot(titanic['Age'], shade=True) #filing the area curve with color
sns.despinec # taking off axis spine
plt.xlabel('Age')


## Conditional Distributions Using A Single Condition. FacetGrid() function

p = sns.FacetGrid(titanic, col = "Pclass", size = 6)
p.map(sns.kdeplot, "Age")
sns.despine(left=True, bottom=True)
plt.plot()


## Creating Conditional Plots Using Two Conditions

g = sns.FacetGrid(titanic, col="Pclass", row="Survived")# row and col parameter provides two different condition
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()


## Creating Conditional Plots Using Three Conditions. 3rd parameter color "hue"

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()


## Adding A Legend

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend() ## added legend for sex
sns.despine(left=True, bottom=True)
plt.show()


## END



