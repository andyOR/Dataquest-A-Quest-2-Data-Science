## In this script, we will learn k-nearest neighbor algorithm


## Introduction

import pandas as pd
nba = pd.read_csv("nba_2013.csv")

# The names of the columns in the data
print(nba.columns.values)


## Understanding the Knn algorithm


## Finding Similar Rows With Euclidean Distance

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

def func(df):
    dist = 0
    for col in distance_columns:
        dist += ((selected_player[col] - df[col]) ** 2)
    return (dist ** (1/2))

lebron_distance = nba.apply(func, axis=1)


## Normalizing column

nba_numeric = nba[distance_columns]

nba_normalized = (nba_numeric - nba_numeric.mean())/nba_numeric.std()


## Finding nearest neighbor

from scipy.spatial import distance
import numpy as np

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values("dist", inplace=True)
second_smallest = distance_frame.iloc[1]["idx"]
most_similar_to_lebron = nba.loc[int(second_smallest)]["player"]


## Generating train and test set

import random
from numpy.random import permutation

# Randomly shuffle the index of nba
random_indices = permutation(nba.index)
# Set a cutoff for how many items we want in the test set (in this case 1/3 of the items)
test_cutoff = math.floor(len(nba)/3)
# Generate the test set by taking the first 1/3 of the randomly shuffled indices
test = nba.loc[random_indices[1:test_cutoff]]
# Generate the train set with the rest of the data
train = nba.loc[random_indices[test_cutoff:]]


## Using scikit learn

# The columns that we'll be using to make predictions
x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
# The column we want to predict
y_column = ["pts"]

from sklearn.neighbors import KNeighborsRegressor
# Create the kNN model
knn = KNeighborsRegressor(n_neighbors=5)
# Fit the model on the training data
knn.fit(train[x_columns], train[y_column])
# Make predictions on the test set using the fit model
predictions = knn.predict(test[x_columns])


## Computing error

actual = test[y_column]

mse =  (((predictions - actual) ** 2).sum()) / len(predictions)













