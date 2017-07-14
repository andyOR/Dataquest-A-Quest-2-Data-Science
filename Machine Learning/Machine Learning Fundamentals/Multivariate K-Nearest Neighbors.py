## In this script, we'll focus on increasing the number of attributes the model uses in machine learning


## Recap from previous script of k-nearest neighbors

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

print(dc_listings.info())


## Removing features

dc_listings.drop(dc_listings.columns[[0,1,2, 4,14, 15,16,17, 18]], axis = 1, inplace = True)


## Handling Missing Values

dc_listings = dc_listings.drop(['cleaning_fee', 'security_deposit'], axis=1)
dc_listings = dc_listings.dropna(axis=0)
print(dc_listings.isnull().sum())


## Normalize Columns

normalized_listings = (dc_listings - dc_listings.mean())/(dc_listings.std())
normalized_listings['price'] = dc_listings['price']
print(normalized_listings.head(3))


## Euclidean Distance For Multivariate Case

from scipy.spatial import distance
first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
fifth_listing = normalized_listings.iloc[4][['accommodates', 'bathrooms']]
first_fifth_distance = distance.euclidean(first_listing, fifth_listing)
print(first_fifth_distance)


## Introduction To Scikit-Learn

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor()

knn = KNeighborsRegressor(algorithm='brute')


## Fitting A Model And Making Predictions

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn = KNeighborsRegressor(n_neighbors = 5, algorithm='brute')
train_features = train_df[['accommodates', 'bathrooms']]
train_target = train_df['price']
knn.fit(train_features, train_target)

predictions = knn.predict(test_df[['accommodates', 'bathrooms']])
print(predictions)


## Calculating MSE Using Scikit-Learn

from sklearn.metrics import mean_squared_error

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse = mean_squared_error(test_df["price"], predictions)
two_features_rmse = (two_features_mse) ** (1/2)

print(two_features_mse)
print(two_features_rmse)


## Using More Features

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]


features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
train_target = train_df['price']
knn.fit(train_df[features], train_target)

four_predictions = knn.predict(test_df[features])

four_mse = mean_squared_error(test_df["price"], four_predictions)
four_rmse = (four_mse) ** (1/2)

print(four_mse)
print(four_rmse)


## Using All Features

features = train_df.columns.tolist()
features.remove('price')
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
train_target = train_df['price']
knn.fit(train_df[features], train_target)

all_features_predictions = knn.predict(test_df[features])

all_features_mse = mean_squared_error(test_df["price"], all_features_predictions)
all_features_rmse = (all_features_mse) ** (1/2)

print(all_features_mse)
print(all_features_rmse)


## END

























