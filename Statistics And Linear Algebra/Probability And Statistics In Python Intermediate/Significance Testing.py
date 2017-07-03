## In this mission, we'll learn about hypothesis testing and statistical significance.

## A hypothesis is a pattern or rule about a process in the world that can be tested


## Hypothesis Testing

# We first set up a null hypothesis that describes the status quo. We then state an alternative hypothesis, which we used to compare with the null hypothesis to decide which describes the data better. In the end, we either need to:

# reject the null hypothesis and accept the alternative hypothesis or
# accept the null hypothesis and reject the alternative hypothesis


## Research Design

# Understanding the research design for a study is an important first step that informs the rest of your analysis. It helps us uncover potential flaws in the study that we need to keep in mind as we dive deeper


## Statistical Significance

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()


## Test Statistic

import numpy as np

mean_difference = mean_group_b - mean_group_a 
print(mean_difference)


## Permutation Test

mean_difference = 2.52
print(all_values)
mean_differences = []

for i in range(0,1000):
    group_a = []
    group_b = []
    for r in all_values:
        p = numpy.random.rand()
        if p >= 0.5:
            group_a.append(r)
        else:
            group_b.append(r)
    
    a = numpy.mean(group_a)
    b = numpy.mean(group_b)
    iteration_mean_difference = b-a
    mean_differences.append(iteration_mean_difference)
    
    
plt.hist(mean_differences)
plt.show()


## Sampling Distribution

sampling_distribution = {}

for r in mean_differences:
    if sampling_distribution.get(r, False):
        # If in the dictionary, grab the value, increment by 1, reassign.
        val = sampling_distribution.get(r)
        inc = val + 1
        sampling_distribution[r] = inc
    else:
        # If not in the dictionary, assign `1` as the value to that key.
        sampling_distribution[r] = 1



## P Value

frequencies = []

for i in sampling_distribution.keys():
    if  i >= 2.52:
        frequencies.append(sampling_distribution[i])
        
sum_freq = np.sum(frequencies)
p_value = sum_freq/1000

## Since the p value of 0 is less than the threshold we set of 0.05, we conclude that the difference in weight lost can't be attributed to random chance alone. We therefore reject the null hypothesis and accept the alternative hypothesis


## END


























