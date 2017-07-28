## In this script, we will try to estimate the leaning rate using a linear regression and interpret its coefficient and statistics


## Introduction To The Data

import pandas
import matplotlib.pyplot as plt

pisa = pandas.DataFrame({"year": range(1975, 1988), 
                         "lean": [2.9642, 2.9644, 2.9656, 2.9667, 2.9673, 2.9688, 2.9696, 
                                  2.9698, 2.9713, 2.9717, 2.9725, 2.9742, 2.9757]})

print(pisa)
plt.scatter(pisa['year'], pisa['lean'])
plt.show()


## Fit The Linear Model

import statsmodels.api as sm

y = pisa.lean # target
X = pisa.year  # features
X = sm.add_constant(X)  # add a column of 1's as the constant term

# OLS -- Ordinary Least Squares Fit
linear = sm.OLS(y, X)
# fit model
linearfit = linear.fit()
linearfit.summary()


## Define A Basic Linear Model

# Our predicted values of y
yhat = linearfit.predict(X)
print(yhat)

residuals = yhat - y


## Histogram Of Residuals

# The variable residuals is in memory
plt.hist(residuals, 5)


## InterpretationOf Histogram



## Sum Of Squares

import numpy as np

# sum the (predicted - observed) squared
SSE = np.sum((y.values-yhat)**2)

RSS = np.sum((np.mean(y.values)-yhat)**2)

TSS = np.sum((y.values - np.mean(y.values))**2)


## R-Squared

SSE = np.sum((y.values-yhat)**2)
ybar = np.mean(y.values)
RSS = np.sum((ybar-yhat)**2)
TSS = np.sum((y.values-ybar)**2)

R2 = 1 - SSE/TSS


## Interpretation Of R-Squared


## Coefficients Of The Linear Model

# Print the models summary
#print(linearfit.summary())

#The models parameters
print("\n",linearfit.params)
delta = linearfit.params["year"] * 15


## Variance Of Coefficients

# Enter your code here.
# Compute SSE
SSE = np.sum((y.values - yhat)**2)
# Compute variance in X
xvar = np.sum((pisa.year - pisa.year.mean())**2)
# Compute variance in b1 
s2b1 = SSE / ((y.shape[0] - 2) * xvar)


## T-Distribution

from scipy.stats import t

# 100 values between -3 and 3
x = np.linspace(-3,3,100)

# Compute the pdf with 3 degrees of freedom
print(t.pdf(x=x, df=3))

tdist3 = t.pdf(x=x, df=3)
tdist30 = t.pdf(x=x, df=30)
plt.plot(tdist3, tdist30)


## Statistical Significance Of Coefficients

# The variable s2b1 is in memory.  The variance of beta_1

tstat = np.absolute(linearfit.params['year'] - 0)/(s2b1) ** (1/2)


## The P-Value

# At the 95% confidence interval for a two-sided t-test we must use a p-value of 0.975
pval = 0.975

# The degrees of freedom
df = pisa.shape[0] - 2

# The probability to test against
p = t.cdf(tstat, df=df)

beta1_test = p > pval


## END










































