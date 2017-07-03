## In this mission, we'll be learning about the chi-squared test for categorical data.
## This test enables us to determine the statistical significance of observing a set of categorical values

## This is where a chi-squared test can help.
## The chi-squared test enables us to quantify the difference between sets of observed and expected categorical values


## Calculating Differences

female_diff = (10771 - 16280.5) / 16280.5
male_diff = (21790 - 16280.5) / 16280.5


## Updating The Formula

female_diff = (10771 - 16280.5) ** 2 / 16280.5
male_diff = (21790 - 16280.5) ** 2 / 16280.5
gender_chisq = female_diff + male_diff


## Generating A Distribution

chi_squared_values = []
from numpy.random import random
import matplotlib.pyplot as plt

for i in range(1000):
    sequence = random((32561,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    a = len(sequence[sequence == 0])
    b = len(sequence[sequence == 1])    
    female_diff = (a - 16280.5) ** 2 / 16280.5
    male_diff = (b - 16280.5) ** 2 / 16280.5
    gender_chisq = female_diff + male_diff
    chi_squared_values.append(gender_chisq)
    
    
    
plt.hist(chi_squared_values)
plt.show()


## Statistical Significance

# Now that we have a chi-squared sampling distribution, we can compare the chi-squared value we calculated for our data to it to see if our result is statistically significant.
# The chi-squared value we calculated was 3728.95.
# The highest value in the chi-squared sampling distribution was about 12.
# This means that our chi-squared value is higher than 100% of all the values in the sampling distribution, so we get a p-value of 0


## Smaller Samples

female_diff = (107.71 - 162.805) ** 2 / 162.805
male_diff = (217.90- 162.805)** 2 / 162.805
gender_chisq = female_diff + male_diff


## Sampling Distribution Equality

# As sample sizes get larger, seeing large deviations from the expected probabilities gets less and less likely
# The chi-squared value follows the same principle.
# Chi-squared values for the same sized effect increase as sample size increases, but the chance of getting a high chi-squared value decreases as the sample gets larger


chi_squared_values = []

from numpy.random import random
import matplotlib.pyplot as plt

for i in range(1000):
    sequence = random((300,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    a = len(sequence[sequence == 0])
    b = len(sequence[sequence == 1])    
    female_diff = (a - 150) ** 2 / 150
    male_diff = (b - 150) ** 2 / 150
    gender_chisq = female_diff + male_diff
    chi_squared_values.append(gender_chisq)
    
    
    
plt.hist(chi_squared_values)
plt.show()


## Degrees Of Freedom

# A degree of freedom is the number of values that can vary without the other values being "locked in".
# In the case of our two categories, there is actually only one degree of freedom


## Increasing Degrees Of Freedom

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)
    
race_chisq = sum(diffs)



## Using SciPy

from scipy.stats import chisquare
import numpy as np

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
chisquare_value, pvalue = chisquare(observed, expected)
race_pvalue = pvalue



## END
















































