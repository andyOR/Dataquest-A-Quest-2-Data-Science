## Reading the dataset "fandango_score_comparison.csv"

import pandas as pd
movies = pd.read_csv("fandango_score_comparison.csv")
movies.head()


## Histograms

import matplotlib.pyplot as plt
%matplotlib inline
plt.hist(movies["Metacritic_norm_round"])
plt.show()
plt.hist(movies["Fandango_Stars"])
plt.show()


## Mean, Median, And Standard Deviation

import numpy as np
mean_mc = sum(movies["Metacritic_norm_round"])/len(movies["Metacritic_norm_round"])
mean_fd = sum(movies["Fandango_Stars"])/len(movies["Fandango_Stars"])
median_mc = np.median(movies["Metacritic_norm_round"])
median_fd = np.median(movies["Fandango_Stars"])
std_mc = np.std(movies["Metacritic_norm_round"])

std_fd = np.std(movies["Fandango_Stars"])
print(mean_mc)
print(mean_fd)
print(median_mc)
print(median_fd)
print(std_mc)
print(std_fd)


## Scatter Plots

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"] )
movies["fm_diff"] = np.absolute(movies["Metacritic_norm_round"] - movies["Fandango_Stars"])
movies["fm_diff"][::-1].sort()
movies.sort_values(by="fm_diff", ascending=False).head(5)


## Correlations

from scipy.stats.stats import pearsonr
import numpy as np
r, p_value = pearsonr(movies["Fandango_Stars"], movies["Metacritic_norm_round"])
from scipy.stats import linregress
slope, intercept, r_value, p_value, stderr_slope = linregress(movies["Metacritic_norm_round"], movies["Fandango_Stars"]) 
listwith3 = movies["Metacritic_norm_round"][movies["Metacritic_norm_round"]==3.0]
pred_3 = np.asarray([slope * x + intercept for x in listwith3])
listfd = movies["Fandango_Stars"][movies["Metacritic_norm_round"]==3.0]
print(pred_3, listfd)


## Residuals

print(slope)
print(intercept)
pred_1 = 1 * slope + intercept
pred_5 = 5 * slope + intercept
plt.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
plt.plot([1,5],[pred_1,pred_5])
plt.xlim(1,5)



## ENDplt.show()
