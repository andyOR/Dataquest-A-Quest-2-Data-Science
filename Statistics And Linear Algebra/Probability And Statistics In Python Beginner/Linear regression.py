## In this script, we'll learn linear regression using dataset of how expert wine tasters evaluated different white wines

## we'll learn how to use linear regression to make predictions about wine quality using existing data


## Drawing Lines

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
# Going by our formula, every y value at a position is the same as the x-value in the same position.
# We could write y = x, but let's write them all out to make this more clear.
y = [0, 1, 2, 3, 4, 5]

# As you can see, this is a straight line that passes through the points (0,0), (1,1), (2,2), and so on.
plt.plot(x, y)
plt.show()

# Let's try a slightly more ambitious line.
# What if we did y = x + 1?
# We'll make x an array now, so we can add 1 to every element more easily.
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 1

# y is the same as x, but every element has 1 added to it.
print(y)

# This plot passes through (0,1), (1,2), and so on.
# It's the same line as before, but shifted up 1 on the y-axis.
plt.plot(x, y)
plt.show()

# By adding 1 to the line, we moved what's called the y-intercept -- where the line intersects with the y-axis.
# Moving the intercept can shift the whole line up (or down when we subtract).
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x -1

plt.plot(x, y)
plt.show()

x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 10

plt.plot(x, y)
plt.show()



## Working With Slope

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y = 2 * x

# See how this line is "steeper" than before?  The larger the slope is, the steeper the line becomes.
# On the flipside, fractional slopes will create a "shallower" line.
# Negative slopes will create a line where y values decrease as x values increase.
plt.plot(x, y)
plt.show()

y = 4 * x
plt.plot(x, y)
plt.show()

y = 0.5 * x
plt.plot(x, y)
plt.show()

y = -2 * x
plt.plot(x, y)
plt.show()


## Starting Out With Linear Regression

# The wine quality data is loaded into wine_quality
from numpy import cov

cov = cov(wine_quality["density"], wine_quality["quality"])[0,1]
slope_density = cov/(wine_quality["density"].var())


## Finishing Linear Regression

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

intercept_density = wine_quality["quality"].mean() - calc_slope(wine_quality["density"], wine_quality["quality"])* wine_quality["density"].mean()


## Making Predictions

from numpy import cov

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

# Calculate the intercept given the x column, y column, and the slope
def calc_intercept(x, y, slope):
  return y.mean() - (slope * x.mean())

def predict(col):
    return calc_slope(wine_quality["density"], wine_quality["quality"]) * col + calc_intercept(wine_quality["density"], wine_quality["quality"], calc_slope(wine_quality["density"], wine_quality["quality"]))

predicted_quality = wine_quality["density"].apply(predict)


## Finding Error

# The linregress function makes it simple to do linear regression

from scipy.stats import linregress

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- for now, don't worry about them.
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)
print(intercept)


predicted_y = numpy.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)


## Standard Error

from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)

s_e = (rss/(len(wine_quality["quality"])-2))** (1/2)

dist_from_actual = [float(wine_quality["quality"][i] -  predicted_y[i]) for i in range(0, len(predicted_y))]

percent_one = []
percent_two = []
percent_three = []
for i in dist_from_actual:
    if i < s_e:
        if i > -s_e:
            percent_one.append(i)
    if i < 2*s_e:
        if i > -2*s_e:
            percent_two.append(i)
    if i < 3*s_e:
        if i > -3*s_e:
            percent_three.append(i)
            
within_one = (len(percent_one)/len(predicted_y))
within_two = (len(percent_two)/len(predicted_y))
within_three = (len(percent_three)/len(predicted_y))


## END
