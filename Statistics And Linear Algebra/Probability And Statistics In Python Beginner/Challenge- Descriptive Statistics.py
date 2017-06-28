## In this challenge, we'll practice the statistical techniques we learned in the previous missions

## We'll be working with the file fandango_score_comparison.csv, which you can download from
## https://github.com/fivethirtyeight/data/tree/master/fandango


## Introduction

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5,12))
ax1.grid(color='b', linestyle='-', linewidth=2)
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)


ax1.hist(movie_reviews["RT_user_norm"])
ax1.set_xlim(0.0, 5.0)
ax1.grid(color='b', linestyle='-', linewidth=1)
ax2.hist(movie_reviews["Metacritic_user_nom"])
ax2.set_xlim(0.0, 5.0)
ax2.grid(color='b', linestyle='-', linewidth=1)
ax3.hist(movie_reviews["Fandango_Ratingvalue"])
ax3.set_xlim(0.0, 5.0)
ax3.grid(color='b', linestyle='-', linewidth=1)
ax4.hist(movie_reviews["IMDB_norm"])
ax4.set_xlim(0.0, 5.0)
ax4.grid(color='b', linestyle='-', linewidth=1)
plt.show()
