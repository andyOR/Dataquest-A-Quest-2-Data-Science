## In this course, we've explored two different ways to find the solution to Ax=b when b isn't a vector containing all zeroes



## Inconsistent Systems

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,1000)

y1 = 5/4 - 2*x
y2 = 5/2 - 2*x

plt.plot(x, y1, color = 'blue')
plt.plot(x, y2, color = 'blue')
plt.show()


## Singular Matrix


## Possible Solutions For Nonhomogenous Systems


## Homogenous Systems

def test_homog(x3):
    x1 = float(4/3*x3)
    x2 = 0
    return((3*x1 + 5*x2 - 4*x3 == 0) and (x2 == 0))

b_one = test_homog(1)
b_ten = test_homog(-10)


END

