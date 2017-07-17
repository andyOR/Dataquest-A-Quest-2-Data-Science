## In this script, we'll learn more about column vectors and their associated operations to help us understand certain properties of linear systems


## From Matrices To Vectors


## Geometric Intuition Of Vectors

import numpy as np

# This code draws the x and y axis as lines.
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-3,3)
plt.ylim(-4,4)

# Add your code here.
plt.quiver(0, 0, 2, 3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, -2, -3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='gold')
plt.quiver(0, 0, 2, 2, angles='xy', scale_units='xy', scale=1, color='gold')


## Vector Operations

# This code draws the x and y axis as lines.
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-4,4)
plt.ylim(-1,4)

# Add your code here.
plt.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(3, 0, 0, 3, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0, 0, 3, 3, angles='xy', scale_units='xy', scale=1, color='green')


## Scaling Vectors

# This code draws the x and y axis as lines.
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(0,10)
plt.ylim(0,5)

# Add your code here.
plt.quiver(0, 0, 3, 1, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 6, 2, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0, 0, 9, 3, angles='xy', scale_units='xy', scale=1, color='orange')


## Vectors In NumPy

import numpy as np

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],[0],[1]], dtype = np.float32)
vector_linear_combination = 2 * vector_one + 5 * vector_two


## Dot Product

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

dot_product = np.dot(vector_one[:,0], vector_two)
print(dot_product)


##  Linear Combination

w = np.asarray([
    [1],[2]], dtype= np.float32)
v = np.asarray([
    [3],[1]], dtype=np.float32)

end_point = 2 *v - w * 2


## Linear Combination And Vectors


## The Matrix Equation


## END








