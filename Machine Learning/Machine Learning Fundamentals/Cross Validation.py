## In this script, we'll focus on more robust techniques of cross validation


## Introduction

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.reindex(shuffled_index)

split_one = dc_listings.iloc[0:1862]
split_two = dc_listings.iloc[1862:]

## Holdout Validation

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one
# First half
model = KNeighborsRegressor()
model.fit(train_one[["accommodates"]], train_one["price"])
test_one["predicted_price"] = model.predict(test_one[["accommodates"]])
iteration_one_rmse = mean_squared_error(test_one["price"], test_one["predicted_price"])**(1/2)

# Second half
model.fit(train_two[["accommodates"]], train_two["price"])
test_two["predicted_price"] = model.predict(test_two[["accommodates"]])
iteration_two_rmse = mean_squared_error(test_two["price"], test_two["predicted_price"])**(1/2)

avg_rmse = np.mean([iteration_two_rmse, iteration_one_rmse])

print(iteration_one_rmse, iteration_two_rmse, avg_rmse)


## K-Fold Cross Validation

dc_listings.set_value(dc_listings.index[0:744], "fold", 1)
dc_listings.set_value(dc_listings.index[744:1488], "fold", 2)
dc_listings.set_value(dc_listings.index[1488:2232], "fold", 3)
dc_listings.set_value(dc_listings.index[2232:2976], "fold", 4)
dc_listings.set_value(dc_listings.index[2976:3723], "fold", 5)


##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
# Training
model = KNeighborsRegressor()
train_iteration_one = dc_listings[dc_listings["fold"] != 1]
test_iteration_one = dc_listings[dc_listings["fold"] == 1]
model.fit(train_iteration_one[["accommodates"]], train_iteration_one["price"])


model.fit(train_iteration_one[["accommodates"]], train_iteration_one["price"])

# Predicting
labels = model.predict(test_iteration_one[["accommodates"]])
test_iteration_one["predicted_price"] = labels
iteration_one_mse = mean_squared_error(test_iteration_one["price"], test_iteration_one["predicted_price"])
iteration_one_rmse = iteration_one_mse ** (1/2)


## Function For Training Models

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_validate(df, folds):
    # Training
    model = KNeighborsRegressor()
    train_iteration_one = dc_listings[dc_listings["fold"] != folds]
    test_iteration_one = dc_listings[dc_listings["fold"] == folds]
    model.fit(train_iteration_one[["accommodates"]], train_iteration_one["price"])
    # Predicting
    labels = model.predict(test_iteration_one[["accommodates"]])
    test_iteration_one["predicted_price"] = labels
    iteration_one_mse = mean_squared_error(test_iteration_one["price"], test_iteration_one["predicted_price"])
    rmse = iteration_one_mse ** (1/2)
    return rmse

rmses = []
for r in fold_ids:
    rmse1 = train_and_validate(dc_listings, r)
    rmses.append(rmse1)
    
avg_rmse = np.mean(rmses)

print(rmses)
print(avg_rmse)

## Performing K-Fold Cross Validation Using Scikit-Learn

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
kf = KFold(len(dc_listings), 5, shuffle=True, random_state=1)
model = KNeighborsRegressor()
mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="mean_squared_error", cv=kf)
rmses = [np.sqrt(np.absolute(mse)) for mse in mses]
avg_rmse = np.mean(rmses)

print(rmses)
print(avg_rmse)


## Exploring Different K Values

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(len(dc_listings), fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="mean_squared_error", cv=kf)
    rmses = [np.sqrt(np.absolute(mse)) for mse in mses]
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))


## END

