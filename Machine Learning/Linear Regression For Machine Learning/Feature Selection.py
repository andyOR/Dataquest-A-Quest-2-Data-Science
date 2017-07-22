## In this script, we'll explore how to use correlation between features and the target column, correlation between features, and variance of features to select features.


## Missing Values

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
numerical_train = train.select_dtypes(include=['int', 'float'])
numerical_train = numerical_train.drop(['PID', 'Year Built', 'Year Remod/Add','Garage Yr Blt', 'Mo Sold','Yr Sold'], axis = 1)
null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)


## Correlating Feature Columns With Target Column

train_subset = train[full_cols_series.index]
correlations = train_subset.corr()
sorted_corrs = correlations['SalePrice'].abs().sort_values()
print(sorted_corrs)


## Correlation Matrix Heatmap

import seaborn as sns
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,6))
strong_corrs = sorted_corrs[sorted_corrs > 0.3]
corrmat = train_subset[strong_corrs.index].corr()
sns.heatmap(corrmat)


## Train And Test Model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
test = test[final_corr_cols.index]
clean_test = test.dropna()
lr = LinearRegression()
lr.fit(train[features], train[target])
predictions_train = lr.predict(train[features])
predictions_test = lr.predict(clean_test[features])

train_rmse = (mean_squared_error(train[target], predictions_train))** (1/2)
test_rmse = (mean_squared_error(clean_test[target], predictions_test))** (1/2)


## Removing Low Variance Features

unit_train = train[features]/(train[features].max())
sorted_vars = unit_train.var().sort_values()
print(sorted_vars)


## Final Model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

features = features.drop(['Open Porch SF'])
lr = LinearRegression()
lr.fit(train[features], train[target])
predictions_train = lr.predict(train[features])
predictions_test = lr.predict(clean_test[features])

train_rmse_2 = (mean_squared_error(train[target], predictions_train))** (1/2)
test_rmse_2 = (mean_squared_error(clean_test[target], predictions_test))** (1/2)

## END
