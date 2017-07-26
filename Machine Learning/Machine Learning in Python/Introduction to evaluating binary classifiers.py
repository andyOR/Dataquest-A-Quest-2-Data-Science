## Introduction To The Data

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])

labels = model.predict(admissions[['gpa']])
admissions['predicted_label'] = labels
print(admissions['predicted_label'].value_counts())
print(admissions.head())


## Accuracy

admissions['actual_label'] = admissions['admit']
matches = admissions['actual_label']==admissions['predicted_label']
correct_predictions = admissions[matches==True]
print(correct_predictions.head())
accuracy = float(len(correct_predictions)/admissions.shape[0])
print(accuracy)


## Binary Classification Outcomes

true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

print(true_positives)
print(true_negatives)


## Sensitivity

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_n = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_n])
sensitivity = true_positives/(true_positives + false_negatives)
print(sensitivity)


## Specificity

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

false_p = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)
false_positives = len(admissions[false_p])
specificity = true_negatives / (false_positives + true_negatives)
print(specificity)


## END
