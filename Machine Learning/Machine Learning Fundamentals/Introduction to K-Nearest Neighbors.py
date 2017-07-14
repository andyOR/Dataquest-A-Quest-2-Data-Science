## The process of discovering patterns in existing data to make a prediction is called machine learning
## In this script, we'll explore a specific machine learning technique called k-nearest neighbors

## we will be working with "dc_airbnb.csv" contains dataset from october 2015 on specific listing that's available for renting on AirBnB in the Washington, D.C. area

## Introduction To The Data

import pandas as pd
dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings.head())


## K-Nearest Neighbors


## Euclidean Distance

import numpy as np
first_distance = np.absolute(dc_listings["accommodates"][0] - 3)
print(first_distance)


## Calculate Distance For All Observations

import numpy as np
def dist(row):
    r = row - 3
    return np.absolute(r)

dc_listings["distance"] = dc_listings["accommodates"].apply(dist)
print(dc_listings["distance"].value_counts())


## Randomizing, And Sorting

import numpy as np
np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings.iloc[0:10]['price'])


## Average Price

stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollar = stripped_commas.str.replace('$', '')
dc_listings["price"] = stripped_dollar.astype(float)
mean_price = dc_listings.iloc[0:5]['price'].mean()
print(mean_price)


## Function To Make Predictions

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    predict = temp_df.iloc[0:5]['price'].mean()
    return (predict)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)


## END
