## In this script, we'll explore a technique called ordinary least squares estimation or OLS estimation for short


## Introduction

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']
X = train[features]
y = train['SalePrice']
a = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)),np.dot(np.transpose(X), y))


## Cost Function


## Derivative Of The Cost Function


## Gradient Descent Vs. Ordinary Least Squares


## END
