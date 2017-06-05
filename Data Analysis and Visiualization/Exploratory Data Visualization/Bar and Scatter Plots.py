## In this script, we will learn about bar and scatter plots.
## We will be using movie rating data in this script


## Introduction To The Data

import pandas as pd

reviews = pd.read_csv("fandango_scores.csv")
#print(reviews.columns)
norm_reviews = reviews[["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]
norm_reviews.loc[0]


## Bar Plot. We need a visualization that scales graphical objects to the quantitative values
## we're interested in comparing. One of these visualizations is a bar plot.


## Creating Bars

import matplotlib.pyplot as plt
from numpy import arange

# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews.ix[0, num_cols].values
# Positions of the left sides of the bars. [0.75, 1.75, 2.75, 3.75, 4.75]
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots() # pyplot.subplots() to first generate a single subplot and return both the Figure and Axes object
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()


## Aligning Axis Ticks And Labels

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)

ax.set_xticks(tick_positions) #x-axis tick positions
ax.set_xticklabels(num_cols, rotation=90) #x-axis tick labels and rotation
ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()


## Horizontal Bar Plot

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5)

ax.set_yticks(tick_positions) #yaxis tick positions
ax.set_yticklabels(num_cols) #yaxis tick labels and rotation
ax.set_ylabel("Rating Source")
ax.set_xlabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()


## Scatter Plot

fig, ax = plt.subplots()

ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm']) # creating scatter plot
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()


## Switching Axes. Axes switched and plotted one above other

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")

ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel("Rotten Tomatoes")
ax2.set_ylabel("Fandango")

plt.show()


## Benchmarking Correlation. Comparing fandango with all othher three ratings

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)


ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)

ax3.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)

plt.show()


## END

