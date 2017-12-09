## In this script, we're going work with two new algorithms: k-nearest neighbors
## and random forests as model selection technique


## Introducing model selection

import pandas as pd
train = pd.read_csv("train_modified.csv")
holdout = pd.read_csv("holdout_modified.csv")


## Training a base line model

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

all_X = train.drop(['Survived','PassengerId'],axis=1)
all_y = train['Survived']

lr = LogisticRegression()

scores = cross_val_score(lr, all_X, all_y, cv=10)
accuracy_lr = np.mean(scores)


## Training model using k-nearest neighbors

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

scores = cross_val_score(knn, all_X, all_y,cv=10)
accuracy_knn = np.mean(scores)


## Exploring different k values

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

def plot_dict(dictionary):
    pd.Series(dictionary).plot.bar(figsize=(9,6),
                                   ylim=(0.78,0.83),rot=0)
    plt.show()

knn_scores = dict()

for k in range(1,50,2):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, all_X, all_y,cv=10)
    knn_scores[k] = np.mean(scores)
    
plot_dict(knn_scores)


## Automating Hyperparameter Optimization with Grid Search

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

hyperparameters = {
    "n_neighbors": range(1,20,2),
    "weights": ["distance", "uniform"],
    "algorithm": ['brute'],
    "p": [1,2]
}

knn = KNeighborsClassifier()
grid = GridSearchCV(knn, param_grid=hyperparameters, cv=10)
grid.fit(all_X, all_y)

best_params = grid.best_params_
best_score = grid.best_score_


## Submitting K-Nearest Neighbors Predictions to Kaggle

holdout_no_id = holdout.drop(['PassengerId'],axis=1)
best_knn = grid.best_estimator_
holdout_predictions = best_knn.predict(holdout_no_id)

submission = pd.DataFrame({
    "PassengerId":holdout["PassengerId"],
    "Survived":holdout_predictions
})

submission.to_csv("submission_1.csv", index=False)


## Introducing Random Forests

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=1)
scores = cross_val_score(clf, all_X, all_y, cv=10)
accuracy_rf = scores.mean()


## Tuning RF parameters

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

hyperparameters = {"criterion": ["entropy", "gini"],
                   "max_depth": [5, 10],
                   "max_features": ["log2", "sqrt"],
                   "min_samples_leaf": [1, 5],
                   "min_samples_split": [3, 5],
                   "n_estimators": [6, 9]
}

clf = RandomForestClassifier(random_state=1)
grid = GridSearchCV(clf,param_grid=hyperparameters,cv=10)

grid.fit(all_X, all_y)

best_params = grid.best_params_
best_score = grid.best_score_


## Submitting Random Forest Predictions to Kaggle

best_rf = grid.best_estimator_

holdout_predictions = best_rf.predict(holdout_no_id)

submission = pd.DataFrame({
    "PassengerId":holdout["PassengerId"],
    "Survived":holdout_predictions
})

submission.to_csv("submission_2.csv", index=False)






































