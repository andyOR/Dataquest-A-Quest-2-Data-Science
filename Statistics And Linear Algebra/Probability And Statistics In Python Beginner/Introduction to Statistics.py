## Introduction To Scales


import numpy as np
car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
mean_car_speed = np.mean(car_speeds)
mean_earthquake_intensities = np.mean(earthquake_intensities)


## Discrete And Continuous Scales

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt

plt.plot(day_numbers, snail_crawl_length)
plt.show()
plt.plot(day_numbers, cars_in_parking_lot)
plt.show()


## Understanding Scale Starting Points

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]
degrees_zero = []
for i in fahrenheit_degrees:
    r = i + (459.67)
    degrees_zero.append(r)
population_zero = yearly_town_population


## Working With Ordinal Scales

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)


## Grouping Values With Categorical Scales

# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
male_list_savings = []
female_list_savings = []
for i in range(0, len(savings)):
    if gender[i] == "male":
        male_list_savings.append(savings[i])
    else:
        female_list_savings.append(savings[i])

        female_list_savings.append(savings[i])
        
male_savings = sum(male_list_savings)/len(male_list_savings)
        
male_savings = sum(male_list_savings)/len(male_list_savings)
female_savings = sum(female_list_savings)/len(female_list_savings)


## Visualizing Counts With Frequency Histograms

# Let's say that we watch cars drive by and calculate average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()

# Let's say we measure student test scores from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]
plt.hist(student_scores)
plt.show()


## Aggregating Values With Histogram Bins

