## In this guided project, we will clean a new dataset in jupyter notebook

# Dataset included in this project is from star wars data.
# While waiting for Star Wars: The Force Awakens to come out, the team at FiveThirtyEight became interested in answering some questions about Star Wars fans
# Tis dataset can be found here https://github.com/fivethirtyeight/data/tree/master/star-wars-survey


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


## 
