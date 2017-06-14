## In this script, we will learn about other key data structure of Pandas, Dataframes
## We will use movie rating here too, fandango_score_comparison.csv


## Shared Indexes

import pandas as pd

fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango[0:2])
print(fandango.index)


## Using Integer Indexes To Select Rows

fandango = pd.read_csv('fandango_score_comparison.csv')
first_row = 0
last_row = fandango.shape[0] - 1
first_last = fandango.iloc[[first_row, last_row]]


## Using Custom Indexes. set_index() to set an index

fandango = pd.read_csv('fandango_score_comparison.csv')

fandango_films = fandango.set_index("FILM", drop = False)
print(fandango_films.index)


## Using A Custom Index For Selection

best = ["The Lazarus Effect (2015)","Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[best]


## Apply() Logic Over The Columns In A Dataframe. This can be used to apply specific function over the dataframe

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))
print(deviations)


## Apply() Logic Over Columns: Practice

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))

halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))


## Apply() Over Dataframe Rows.

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])

rt_mt_means =  rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_means[0:5])


## End


