## In this script, we'll construct probability distributions

## Binomial Distributions

# Many commonly occurring events can be expressed in terms of binomial outcomes -- a coin flip, winning a football game, the stock market going up, and more
# One easy way to visualize binomials is a binomial distribution. Given N events, it plots the probabilities of getting different numbers of successful outcomes


## Bikesharing Distribution

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
prob_over_5000 = bikes['cnt'][bikes["cnt"] > 5000].shape[0]/ bikes.shape[0]


## Computing The Distribution

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

def find_combination_probability(N, k, p, q):
    # Take p to the power k, and get the first term.
    term_1 = p ** k
    # Take q to the power N-k, and get the second term.
    term_2 = q ** (N-k)
    # Multiply the terms out.
    return term_1 * term_2
outcome_probs = []
for i in outcome_counts:
    p = 0.39
    q = 0.61
    probs = find_outcome_combinations(30, i) * find_combination_probability(30, i, p, q)
    outcome_probs.append(probs)


## Plotting The Distribution


import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()


## Simplifying The Computation

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt


# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,30,0.39)

plt.bar(outcome_counts, dist)
#plt.xlabel("Number of days with more than 5000 riders")
#plt.ylabel("Probability score")
plt.show()


## How To Think About A Probability Distribution

## How To Think About A Probability Distribution

dist_mean = None

dist_mean = 30 * 0.39 # formula = N * p


## Computing The Standard Deviation

dist_stdev = None

dist_stdev = (30 * 0.39 * 0.61) ** (1/2) # sqr.root of N * p * q


## A Different Plot

# Enter your answer here.
import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt


# Create a range of numbers from 0 to 10, with 11 elements (each number has one entry).
outcome_counts = linspace(0,10,11)

# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,10,0.39)

plt.bar(outcome_counts, dist)
#plt.xlabel("Number of days with more than 5000 riders")
#plt.ylabel("Probability score")
plt.show()

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = linspace(0,100,101)

# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,100,0.39)

plt.bar(outcome_counts, dist)
#plt.xlabel("Number of days with more than 5000 riders")
#plt.ylabel("Probability score")
plt.show()


## The Normal Distribution

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()


## Cumulative Density Function

from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

# Create the cumulative binomial probabilities, one for each entry in outcome_counts.
dist = binom.cdf(outcome_counts,30,0.39)

plt.plot(outcome_counts, dist)
plt.show()


## Calculating Z-Scores

left_16 = None
right_16 = None

# The sum of all the probabilities to the left of k, including k.
left_16 = binom.cdf(16,30,0.39)

# The sum of all probabilities to the right of k.
right_16 = 1 - left_16


## END



















































