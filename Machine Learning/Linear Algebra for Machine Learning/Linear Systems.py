## In this course, we'll focus on understanding linear functions

## Overview Of Linear Algebra

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,50,1000)
y1 = 30*x + 1000

y2 = 50*x + 100

plt.plot(x, y1, color = 'orange')
plt.plot(x, y2, color = 'blue')
plt.show()


## Solving Linear Systems By Elimination


## Representing Functions In General Form


## Representing An Augmented Matrix In NumPy

matrix_one = np.asarray([
    [30,-1,-1000],
    [50,-1,-100]
],dtype=np.float32)


## Matrix Representation Of The Solution


## Row Operations

matrix_one = np.asarray([
    [30, -1, -500],
    [50, -1, -100]  
], dtype=np.float32)

matrix_one[0] = matrix_one[0] / 30


## Simplifying Matrix To Echelon Form


## Row Reduced Echelon Form

matrix_three = np.asarray([
    [1, -1/30, -1000/30],
    [0, 1, 2350]  
], dtype=np.float32)

matrix_three[0] = matrix_three[0] + (1/30)*matrix_three[1]

## END









