## In this script, we learned how to test our machine learning models using basic cross validation and different metrics

## Testing Quality Of Predictions

import pandas as pd
import numpy as np
dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbor_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbor_prices.mean()
    return(predicted_price)

test_df["predicted_price"] = test_df["accommodates"].apply(predict_price)


## Error Metrics

import numpy as np

mae = sum(np.absolute(test_df["predicted_price"] - test_df["price"]))/len(test_df)


## Mean Squared Error

mse = sum((test_df["predicted_price"] - test_df["price"]) ** 2)/len(test_df)


## Training Another Model

train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbors_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbors_prices.mean()
    return(predicted_price)

test_df["predicted_price"] = test_df["bathrooms"].apply(predict_price)
test_df["squared_error"] = (test_df["predicted_price"] - test_df["price"]) ** 2
mse = test_df["squared_error"].mean()
print(mse)


## Root mean squared error

def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbors_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbors_prices.mean()
    return(predicted_price)

test_df['predicted_price'] = test_df['bathrooms'].apply(lambda x: predict_price(x))
test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)
mse = test_df['squared_error'].mean()
rmse = (mse)**(1/2)


##  Comparing MAE And RMSE

errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 1000])

mae_one = errors_one.mean()
rmse_one = (((errors_one) ** 2).mean()) ** (1/2)

mae_two = errors_two.mean()
rmse_two =  (((errors_two) ** 2).mean()) ** (1/2)



## END

