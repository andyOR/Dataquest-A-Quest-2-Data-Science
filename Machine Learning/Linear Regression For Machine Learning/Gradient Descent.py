## In this script and the next, we'll discuss the 2 most common ways for finding the optimal parameter values for a linear regression model


## Introduction


## Single Variable Gradient Descent


## Derivative Of The Cost Function

def derivative(a1, xi_list, yi_list):
    # Modify this function.
    n = len(xi_list)
    der = 0
    for r in range(0,n):
        der += xi_list[r] * (a1*xi_list[r] - yi_list[r])
    error = (2/n) * der
    return error

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial):
    a1_list = [a1_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        deriv = derivative(a1, xi_list, yi_list)
        a1_new = a1 - alpha*deriv
        a1_list.append(a1_new)
    return(a1_list)

# Uncomment when ready.
param_iterations = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150)



## Understanding Multi Parameter Gradient Descent


## Gradient Of The Cost Function

# Uncomment when ready.
#a0_params, a1_params = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 100, .0000003, 150, 1000)

def a1_derivative(a1, xi_list, yi_list):
    len_data = len(xi_list)
    error = 0
    for i in range(0, len_data):
        error += xi_list[i]*(a1*xi_list[i] - yi_list[i])
    deriv = 2*error/len_data
    return deriv

def a0_derivative(a0, xi_list, yi_list):
    len_data = len(xi_list)
    error = 0
    for i in range(0, len_data):
        error += a0*xi_list[i] - yi_list[i]
    deriv = 2*error/len_data
    return deriv

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial, a0_initial):
    a1_list = [a1_initial]
    a0_list = [a0_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        a0 = a0_list[i]
        
        a1_deriv = a1_derivative(a1, xi_list, yi_list)
        a0_deriv = a0_derivative(a0, xi_list, yi_list)
        
        a1_new = a1 - alpha*a1_deriv
        a0_new = a0 - alpha*a0_deriv
        
        a1_list.append(a1_new)
        a0_list.append(a0_new)
    return(a0_list, a1_list)

a0_params, a1_params = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150, 1000)
print(a0_params)


## Gradient Descent For Higher Dimensions


## END
print(a1_params)
