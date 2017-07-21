## In this script, we'll formalize the idea of slope further and learn how to calculate the slope for nonlinear equations at any given point


## Introduction To Limits


## Defined Vs. Undefined Limits


## Introduction To SymPy

import sympy
x,y = sympy.symbols('x y')
y = x^2 + 1
print(y)


## Limits Using SymPy

import sympy
x2,y = sympy.symbols('x2 y')
limit_one = sympy.limit((-x2**2 +3*x2-1+1)/(2.9-3) , x2, 2.9)
print(limit_one)


## Properties Of Limits I

import sympy
x,y = sympy.symbols('x y')

limit_two = sympy.limit(3*x**2 + 3*x -3, x, 1)

print(limit_two)


## Properties Of Limits II

import sympy
x,y = sympy.symbols('x y')

y = x**3 + 2*x**2 -10*x
limit_three = sympy.limit(y,x,-1)
print(limit_three)



## Undefined Limit To Defined Limit

import sympy
x2, y = sympy.symbols('x2 y')

y = (-(x2)**2 + 3*x2 -1 + 1)/(x2-3)
limit_four = sympy.limit(y,x2,3)
print(limit_four)


## END
