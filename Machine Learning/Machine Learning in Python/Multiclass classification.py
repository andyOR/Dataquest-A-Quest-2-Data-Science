## In this script, we will work with concept of multiclass classification in logistics regression

## We will work with data set "auto.csv" dataset which contains information on various cars.
## For each car, there is information on the technical aspects of the vehicle such as the motor's displacement, the weight of the car, the miles per gallon, and how fast the car accelerates.
## Using this information we will predict the origin of the vehicle, either North America, Europe, or Asia.
## The dataset can be found at https://archive.ics.uci.edu/ml/datasets/Auto+MPG

## Introduction To The Data

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars["origin"].unique()
print(unique_regions)


## Dummy Variables

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)
cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head())


## Multiclass Classification

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
highest_train_row = int(cars.shape[0] * .70)
train = shuffled_cars.iloc[0:highest_train_row]
test = shuffled_cars.iloc[highest_train_row:]


## Training A Multiclass Logistic Regression Model

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]

for origin in unique_origins:
    model = LogisticRegression()
    
    X_train = train[features]
    y_train = train["origin"] == origin

    model.fit(X_train, y_train)
    models[origin] = model


## Testing The Models

testing_probs = pd.DataFrame(columns=unique_origins)  

for origin in unique_origins:
    # Select testing features.
    X_test = test[features]   
    # Compute probability of observation being in the origin.
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]


## Choose The Origin

predicted_origins = testing_probs.idxmax(axis= 1)
print(predicted_origins)

predicted_origins = testing_probs.idxmax(axis= 1)
print(len(predicted_origins))
test["predict"] = predicted_origins
matches = test['origin']==test['predict']
correct_predictions = test[matches==True]
#print(correct_predictions.head())
accuracy = float(len(correct_predictions)/test.shape[0])
print(accuracy)


## END
