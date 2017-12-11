## In this script, we'll learn some of the basic building blocks of natural
## langage processing.

## Introduction

## We will use Hacker news dataset for predicting the number of upvotes
## the articles received, based on their headlines.


## Overview of the data

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()


## Tokenzing headlines

tokenized_headlines = []

for row in submissions["headline"]:
    line = row.split(" ")
    tokenized_headlines.append(line)
    
print(tokenized_headlines)


## Preprocessing tokens to increase accuracy

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)
print(clean_tokenized)


## Assembling a Matrix of Unique Words

import numpy as np
unique_tokens = []
single_tokens = []

for line in clean_tokenized:
    [single_tokens.append(p) for p in line]
    
for word in clean_tokenized:
    for s in word:
        if s in single_tokens:
            if s not in unique_tokens:
                unique_tokens.append(s)
                
counts =pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)


## Counting Token Occurrences

for i, item in enumerate(clean_tokenized):
    for token in item:
        if token in unique_tokens:
            counts.iloc[i][token] += 1


## Removing Columns to Increase Accuracy

word_counts = counts.sum(axis=0)

counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]
print(counts.shape)


## Splitting the dataset

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)


## Making predictions

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)


## Computing error

mse =  (((predictions - y_test) ** 2).sum()) / len(predictions)


#3 END
