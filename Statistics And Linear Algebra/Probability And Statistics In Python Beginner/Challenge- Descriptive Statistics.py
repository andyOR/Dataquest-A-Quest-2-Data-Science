## In this challenge, we'll practice the statistical techniques we learned in the previous missions

## We'll be working with the file fandango_score_comparison.csv, which you can download from
## https://github.com/fivethirtyeight/data/tree/master/fandango


## Introduction

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5,12))
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


## Mean

def calc_mean(cols):
    r = cols.values
    mean = sum(r)/len(r)
    return mean

user_reviews = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews = movie_reviews[user_reviews]
user_reviews = user_reviews.apply(calc_mean)
rt_mean = user_reviews["RT_user_norm"]
mc_mean = user_reviews["Metacritic_user_nom"]
fg_mean = user_reviews["Fandango_Ratingvalue"]
id_mean = user_reviews["IMDB_norm"]
print(rt_mean)
print(mc_mean)
print(fg_mean)
print(id_mean)


## Variance And Standard Deviation

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    sq_deviations = (series - mean) ** 2
    mean_sq_deviations = calc_mean(sq_deviations)
    return mean_sq_deviations

user_reviews = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews = movie_reviews[user_reviews]
user_reviews = user_reviews.apply(calc_variance)
rt_var = user_reviews["RT_user_norm"]
rt_stdev = (rt_var)** (1/2)
mc_var = user_reviews["Metacritic_user_nom"]
mc_stdev = (mc_var)** (1/2)
fg_var = user_reviews["Fandango_Ratingvalue"]
fg_stdev = (fg_var) ** (1/2)
id_var = user_reviews["IMDB_norm"]
id_stdev = (id_var) ** (1/2)

print("Rotten Tomatoes (variance):", rt_var)
print("Metacritic (variance):", mc_var)
print("Fandango (variance):", fg_var)
print("IMDB (variance):", id_var)

print("Rotten Tomatoes (standard deviation):", rt_stdev)
print("Metacritic (standard deviation):", mc_stdev)
print("Fandango (standard deviation):", fg_stdev)
print("IMDB (standard deviation):", id_stdev)


## Scatter Plots

fig = plt.figure(figsize = (4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax1.set_xlim(0.0, 5.0)
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax2.set_xlim(0.0, 5.0)
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
ax3.set_xlim(0.0, 5.0)

plt.show()


##  Covariance

def calc_covariance(cols1, cols2):
    col = len(cols1)
    mean1 = cols1.mean()
    mean2 = cols2.mean()
    difference1 = []
    difference2 = []
    difference3 = 0
    for p in cols1:
        difference = p - mean1
        difference1.append(difference)
    for p in cols2:
        difference = p - mean2
        difference2.append(difference)
    for p in range(0, len(cols1)):
        r = difference1[p] * difference2[p]
        difference3 += r
    return (difference3/len(cols1))

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
print(rt_fg_covar)
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
print(mc_fg_covar)
id_fg_covar =  calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
print(id_fg_covar)


## Correlation

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series_one, series_two):
    cov = calc_covariance(series_one, series_two)
    sigma1 = calc_variance(series_one) ** (1/2)
    sigma2 = calc_variance(series_two) ** (1/2)
    corr = cov/(sigma1*sigma2)
    return corr
    

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
print(rt_fg_corr)
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
print(mc_fg_corr)
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
print(id_fg_corr)


## END




