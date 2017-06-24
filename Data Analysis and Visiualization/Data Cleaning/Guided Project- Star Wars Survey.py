## In this guided project, we will clean a new dataset in jupyter notebook

# Dataset included in this project is from star wars data.
# While waiting for Star Wars: The Force Awakens to come out, the team at FiveThirtyEight became interested in answering some questions about Star Wars fans
# This dataset can be found here https://github.com/fivethirtyeight/data/tree/master/star-wars-survey


## Overview

import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
star_wars.head(10)
star_wars.columns
Response = pd.notnull(star_wars["RespondentID"])
star_wars = star_wars[Response]


## Cleaning And Mapping Yes/No Columns

yes_no = {
    "Yes": True,
    "No": False
}
star_wars["Have you seen any of the 6 films in the Star Wars franchise?"]= star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].map(yes_no)
star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"]= star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].map(yes_no)
star_wars.head(10)


## Cleaning And Mapping Checkbox Columns

import numpy as np
cols = star_wars.columns[3:9]
#print(cols)
yes_no={"Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}
for i in cols:
    star_wars[i]=star_wars[i].map(yes_no)


star_wars = star_wars.rename(columns={
        "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
        "Unnamed: 4": "seen_2",
        "Unnamed: 5": "seen_3",
        "Unnamed: 6": "seen_4",
        "Unnamed: 7": "seen_5",
        "Unnamed: 8": "seen_6"
        })

star_wars.head()


## Cleaning The Ranking Columns

star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)

star_wars = star_wars.rename(columns={
        "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2",
        "Unnamed: 11": "ranking_3",
        "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5",
        "Unnamed: 14": "ranking_6"
        })

star_wars.head()


## Finding The Highest-Ranked Movie

mean_movie = star_wars[star_wars.columns[9:15]].mean()

import matplotlib.pyplot as plt 
%matplotlib inline
plt.bar(range(6), mean_movie)


## Finding The Most Viewed Movie

sum_movie= star_wars[star_wars.columns[3:9]].sum()

import matplotlib.pyplot as plt 
%matplotlib inline
plt.bar(range(6), sum_movie)


## Exploring The Data By Binary Segments

males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]
mean_male_movie = males[males.columns[9:15]].mean()
mean_female_movie = females[females.columns[9:15]].mean()
sum_male_movie = males[males.columns[3:9]].sum()
sum_female_movie = females[females.columns[3:9]].sum()
import matplotlib.pyplot as plt 
%matplotlib inline
plt.bar(range(6), mean_male_movie)
plt.bar(range(6), mean_female_movie)
