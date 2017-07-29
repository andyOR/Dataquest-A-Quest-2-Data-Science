## In this script, we'll provide an overview of how we use a linear regression model to make predictions. We'll use scikit-learn for the model training process, so we can focus on gaining intuition for the model-based learning approach to machine learning

## Introduction

# Dataset - "AmesHousing.txt" conatining dataset on sold houses in Ames, Iowa.

import pandas as pd

data = pd.read_csv("AmesHousing.txt", sep = "\t")
train = data[:1460]
test = data[1460:]
data.info()
target = "SalePrice"



## Simple Linear Regression

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn
fig = plt.figure(figsize=(7,5))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
train.plot(x="Garage Area", y="SalePrice", ax=ax1, kind="scatter")
train.plot(x="Gr Liv Area", y="SalePrice", ax=ax2, kind="scatter")
train.plot(x="Overall Cond", y="SalePrice", ax=ax3, kind="scatter")

plt.show()


## Least Squares

train[['GarageArea', 'GrLivArea', 'OverallCond', 'SalePrice']].corr()
             GarageArea  GrLivArea  OverallCond  SalePrice
GarageArea     1.000000   0.468997    -0.151521   0.623431
GrLivArea      0.468997   1.000000    -0.079686   0.708624
OverallCond   -0.151521  -0.079686     1.000000  -0.077856
SalePrice      0.623431   0.708624    -0.077856   1.000000


## Using Scikit-Learn To Train And Predict

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
print(lr.coef_)
print(lr.intercept_)

a0 = lr.intercept_
a1 = lr.coef_


## Making Predictions

import numpy as np

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
from sklearn.metrics import mean_squared_error
predictions_train = lr.predict(train[['Gr Liv Area']])
predictions_test = lr.predict(test[['Gr Liv Area']])

train_rmse = (mean_squared_error(train['SalePrice'], predictions_train))** (1/2)
test_rmse = (mean_squared_error(test['SalePrice'], predictions_test))** (1/2)


## Multiple Linear Regression

cols = ['Overall Cond', 'Gr Liv Area']

lr = LinearRegression()
lr.fit(train[cols], train['SalePrice'])
from sklearn.metrics import mean_squared_error
predictions_train = lr.predict(train[cols])
predictions_test = lr.predict(test[cols])

train_rmse_2 = (mean_squared_error(train['SalePrice'], predictions_train))** (1/2)
test_rmse_2 = (mean_squared_error(test['SalePrice'], predictions_test))** (1/2)



## END

