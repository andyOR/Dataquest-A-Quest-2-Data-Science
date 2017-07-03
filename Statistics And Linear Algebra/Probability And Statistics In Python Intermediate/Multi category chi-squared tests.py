## In this script, we'll look how to make this same technique applicable to cross tables, that show how two categorical columns interact. 


## Calculating Expected Values

males_over50k = 32561 *.241 * .669
males_under50k = 32561 * .669 * .759
females_over50k = 32561 *0.241 * .331
females_under50k = 32561 *0.759 * .331


## Calculating Chi-Squared

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)


## Finding Statistical Significance

import numpy as np
from scipy.stats import chisquare

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
chisquare_value, pvalue = chisquare(observed, expected)
pvalue_gender_income = pvalue


## Cross Tables

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)


## Finding Expected Values

import numpy as np
from scipy.stats import chi2_contingency
table = pandas.crosstab(income["sex"], [income["race"]])
chisq_value, pvalue, df, expected = chi2_contingency(table)
pvalue_gender_race = pvalue


## 











