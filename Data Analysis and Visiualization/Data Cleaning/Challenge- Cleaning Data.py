## In this challenge, we will clean one of the datasets and amke it ready for analysis

# We will work with avengers dataset. Because the writers killed off and revived many of the superheroes, the team at FiveThirtyEight was curious to explore data from the Marvel Wikia site further


## Exploring The Data

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)


## Filtering Out Bad Data

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"]>1960]


## Consolidating Deaths

def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)


## Verifying Years Since Joining

joined_accuracy_count  = int()

for i in true_avengers["Years since joining"]:
    if 2015 - true_avengers["Year"][i] == true_avengers["Years since joining"][i]:
        joined_accuracy_count +=1


## END
