## In this script, we will learn more about Pandas internal to get an deep idea on how the pandas actually works.
## We will learning about series objects, one of the key data structure of Pandas
## In this script, we will use dataset on user ratings through file "fandango_score_comparison.csv"
## This file can be downloaded from this repository "https://github.com/fivethirtyeight/data/tree/master/fandango"


## Data Structures

import pandas as pd

fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2) # first two rows
fandango.shape


## Integer Indexes

fandango = pd.read_csv('fandango_score_comparison.csv')

series_film = fandango["FILM"]
print(series_film[0:5])

series_rt = fandango["RottenTomatoes"]
print(series_rt[0:5])


## Custom Indexes.This would be helpful to find string values from their names

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = pandas.Series(data = rt_scores, index = film_names) # this will create a list on index and data
series_custom


## Integer Index Preservation. Even though the Series object uses a custom string index, the object still has an internal integer index

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:11]
print(fiveten)


## Reindexing. This will help to sort the list and then give new index for sorted list

original_index = series_custom.index

list_sort = sorted(original_index)
sorted_by_index = series_custom.reindex(index = list_sort)
sorted_by_index


## Sorting. This includes sorting by index and sorting by values

sc2 = series_custom.sort_index()
print(sc2[0:10])

sc3 = series_custom.sort_values()
print(sc3[0:10])


## Transforming Columns With Vectorized Operations. Same as NumPy

series_normalized = series_custom / 20


## Comparing And Filtering.

criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]


# Alignment. Series objects align along indices, and DataFrame objects align along both indices and columns

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_critics + rt_users) / 2
rt_mean


## END

