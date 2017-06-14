import os;
os.chdir('c:\\2017\Work\Github\DATAQUEST\Data Analysis and Visiualization\Exploratory Data Visualization')


import pandas as pd

## Line Chart

##unrate = pd.read_csv("unrate.csv")
##unrate['DATE'] = pd.to_datetime(unrate['DATE'])
##unrate.loc[0:12]
##
##import matplotlib.pyplot as plt
##
##date = unrate["DATE"]
##value = unrate["UNRATE"]
##
##plt.plot(date[0:12], value[0:12])
##plt.xticks(rotation = 90)
##
##plt.xlabel("Month")
##plt.ylabel("Unemployment Rate")
##plt.title("Monthly Unemployment Trends, 1948")
##plt.show()
##
##unrate['MONTH'] = unrate['DATE'].dt.month
##fig = plt.figure(figsize=(10,6))
##colors = ['red', 'blue', 'green', 'orange', 'black']
##for i in range(5):
##    start_index = i*12
##    end_index = (i+1)*12
##    subset = unrate[start_index:end_index]
##    label = str(1948 + i)
##    plt.plot(subset['MONTH'], subset['UNRATE'], c=colors[i], label=label)
##plt.legend(loc='upper left')
##plt.xlabel("Month, Integer")
##plt.ylabel("Unemployment Rate, Percent")
##plt.title("Monthly Unemployment Trends, 1948-1952")
##
##plt.show()

## Bar plot

reviews = pd.read_csv("fandango_score_comparison.csv")
import matplotlib.pyplot as plt
from numpy import arange
norm_reviews = reviews[["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]
##num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
##
##bar_widths = norm_reviews.ix[0, num_cols].values
##bar_positions = arange(5) + 0.75
##tick_positions = range(1,6)
##
##fig, ax = plt.subplots()
##ax.barh(bar_positions, bar_widths, 0.5)
##
##ax.set_yticks(tick_positions) #yaxis tick positions
##ax.set_yticklabels(num_cols) #yaxis tick labels and rotation
##ax.set_ylabel("Rating Source")
##ax.set_xlabel("Average Rating")
##ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
##plt.show()
##
##fig, ax = plt.subplots()
##
##ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
##ax.set_xlabel("Fandango")
##ax.set_ylabel("Rotten Tomatoes")
##plt.show()


## Histograms

##fig = plt.figure(figsize=(10,20))
##ax1 = fig.add_subplot(4,1,1)
##ax2 = fig.add_subplot(4,1,2)
##ax3 = fig.add_subplot(4,1,3)
##ax4 = fig.add_subplot(4,1,4)
##
##ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
##ax1.set_title("Distribution of Fandango Ratings")
##ax1.set_ylim(0, 50)
##ax1.set_ylabel("Frequency")
##
##ax2.hist(norm_reviews['RT_user_norm'], bins=20, range=(0, 5))
##ax2.set_title("Distribution of Rotten Tomatoes Ratings")
##ax2.set_ylim(0, 50)
##ax2.set_ylabel("Frequency")
##
##ax3.hist(norm_reviews['Metacritic_user_nom'], bins=20, range=(0, 5))
##ax3.set_title("Distribution of Metacritic Ratings")
##ax3.set_ylim(0, 50)
##ax3.set_ylabel("Frequency")
##
##ax4.hist(norm_reviews['IMDB_norm'], bins=20, range=(0, 5))
##ax4.set_title("Distribution of IMDB Ratings")
##ax4.set_ylim(0, 50)
##ax4.set_ylabel("Frequency")
##
##plt.show()


## Bar plots

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots(figsize=(15,10))
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols)
ax.set_ylim(0,5)
ax.set_title("Distribution of Movie Ratings - Box Plot")
plt.show()
