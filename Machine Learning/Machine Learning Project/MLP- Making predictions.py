## In this cript, we will make predictions from the features we created in last
## two scripts of data cleaning and preparing features


## Recap

import pandas as pd
loans = pd.read_csv("cleaned_loans_2007.csv")
print(loans.info())


## Picking an error metric

import pandas as pd

tn = (predictions == 0) & (loans["loan_status"] == 0)
tp = (predictions == 1) & (loans["loan_status"] == 1)
fn = (predictions == 0) & (loans["loan_status"] == 1)
fp = (predictions == 1) & (loans["loan_status"] == 0)


## Class imbalance

import pandas as pd
import numpy as np

predictions = pd.Series(numpy.ones(loans.shape[0]))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)


## Logistic Regression

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features = loans.columns.tolist()
features.remove('loan_status')
target  = loans['loan_status']
lr.fit(loans[features],target)
predictions = lr.predict(loans[features])


## Cross validation

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold
lr = LogisticRegression()
kf = KFold(features.shape[0], random_state=1)

predictions = cross_val_predict(lr, features, target, cv = kf)
predictions = pd.Series(predictions)

fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)


## Penalizing the classifier

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict

lr = LogisticRegression(class_weight = 'balanced')
kf = KFold(features.shape[0], random_state = 1)

predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)

fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)


## Manual Penalties

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict

penalty = {
    0: 10,
    1: 1
}
lr = LogisticRegression(class_weight=penalty)
kf = KFold(features.shape[0], random_state = 1)

predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)

fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)


## Rando Forests

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict

lr = RandomForestClassifier(class_weight = 'balanced')
kf = KFold(features.shape[0], random_state = 1)

predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)

fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)


## END

































