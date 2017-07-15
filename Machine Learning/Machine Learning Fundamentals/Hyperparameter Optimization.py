## In this script, we'll focus on the impact of increasing k, the number of nearby neighbors the model uses to make predictions

## Recap

import pandas as pd
train_df = pd.read_csv("dc_airbnb_train.csv")
test_df = pd.read_csv("dc_airbnb_test.csv")


## Hyperparameter Optimization

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = [1,2,3,4,5]
mse_values = []
for r in hyper_params:
        knn = KNeighborsRegressor(n_neighbors = r, algorithm='brute')
        train_columns = ['accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews']
        knn.fit(train_df[train_columns], train_df['price'])
        predictions = knn.predict(test_df[train_columns])
        
        mse_values = mean_squared_error(test_df["price"], predictions)
        print(mse_values)


## Expanding Grid Search


from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)


## Visualizing Hyperparameter Values

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params, mse_values)
plt.show()


## Varying Features And Hyperparameters

hyper_params = [x for x in range(1,21)]
mse_values = list()

features = train_df.columns.tolist()
features.remove('price')

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params, mse_values)
plt.xlabel("hyper paramters")
plt.ylabel("Mean Squared error")
plt.title("Error optimization with different k paramters and all features")
plt.show()


## Practice The Workflow

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[two_features], train_df['price'])
    predictions = knn.predict(test_df[two_features])
    mse = mean_squared_error(test_df['price'], predictions)
    two_mse_values.append(mse)

two_lowest_mse = two_mse_values[0]
two_lowest_k = 1

for k,mse in enumerate(two_mse_values):
    if mse < two_lowest_mse:
        two_lowest_mse = mse
        two_lowest_k = k + 1
    
for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[three_features], train_df['price'])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(test_df['price'], predictions)
    three_mse_values.append(mse)
    
three_lowest_mse = three_mse_values[0]
three_lowest_k = 1

for k,mse in enumerate(three_mse_values):
    if mse < three_lowest_mse:
        three_lowest_mse = mse
        three_lowest_k = k + 1

two_hyp_mse[two_lowest_k] = two_lowest_mse
three_hyp_mse[three_lowest_k] = three_lowest_mse

print(two_hyp_mse)
print(three_hyp_mse)


## END
































