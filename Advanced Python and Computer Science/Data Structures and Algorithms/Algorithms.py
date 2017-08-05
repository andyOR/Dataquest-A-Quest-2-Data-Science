## In this script, we'll see few examples of what an algorithm looks like, and introduce some methods for evaluating their efficiency


## Implementing An Algorithm

# When the algorithm finds Kobe in the data set, store his position in Kobe_position
kobe_position = ""

# Find Kobe in the data set
for r in nba:
    player = r[0]
    if player=="Kobe Bryant":
        kobe_position = r[1]
        

## The Importance Of Modularity And Abstraction


## Linear Search With Modular Code

# player_age returns the age of a player in our NBA data set

def player_age(name):
    for r in nba:
        if r[0] == name:
            return r[2]
    return -1
        
allen_age = player_age("Ray Allen")
durant_age = player_age("Kevin Durant")
shaq_age = player_age("Shaquille O'Neal")


## What Makes An Algorithm Smart?

## Constant Time Algorithms


## Exercise: Recognizing Constant Time Algorithms

# Implementation A: Convert degrees Celcius to degrees Fahrenheit
def celcius_to_fahrenheit(degrees):
    step_1 = degrees * 1.8
    step_2 = step_1 + 32
    return step_2

# Implementation B: Reverse a list
def reverse(ls):
    length = len(ls)
    new_list = []
    for i in range(length):
        new_list[i] = ls[length - i]
    return new_list

# Implementation C: Print a blastoff message after a countdown
def blastoff(message):
    count = 10
    for i in range(count):
        print(count - i)
    print(message)

not_constant = "B"


## A Common Pitfall


## Linear Time Algorithms


## Some Other Algorithms

# Find the length of a list
def length(ls):
    count = 0
    for elem in ls:
        count = count + 1
length_time_complexity = "linear"

# Check whether a list is empty -- Implementation 1
def is_empty_1(ls):
    if length(ls) == 0:
        return True
    else:
        return False
is_empty_1_complexity = "linear"

# Check whether a list is empty -- Implementation 2
def is_empty_2(ls):
    for element in ls:
        return False
    return True
is_empty_2_complexity = "constant"


## Notation For Time Complexity


## Why Time Complexity Matters


## END
