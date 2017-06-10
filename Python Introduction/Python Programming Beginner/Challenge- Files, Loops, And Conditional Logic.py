## In this script, we ill explore a challenge for experimenting with files, loops and conditional logic
## We will use "dq_unisex_names.csv" containing the common unisex names in the United States.
## This was compiled by FiveThirtyEight from social security adinistration website
## https://www.ssa.gov/oact/babynames/limits.html


## Read The File Into A String.

f = open('dq_unisex_names.csv', 'r')
names = f.read()


## Convert The String To A List.

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[0:5]
print(first_five)


## Convert The List Of Strings To A List Of Lists

f = open('dq_unisex_names.csv', 'r')
names = f.read() # first complete list
names_list = names.split('\n') # splitted on "\n" character
nested_list = []
for cr in names_list:
    comma_list = cr.split(',') # creating list in every iteration
    nested_list.append(comma_list)
print(nested_list[0:5])


## Convert Numerical Values

print(nested_list[0:5])
numerical_list = []
for cr in nested_list:
    f = cr[0]
    h = float(cr[1])
    i = [f, h]
    numerical_list.append(i)
print(numerical_list[0:5])


## Filter The List

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for cr in numerical_list:
    if cr[1] >= 1000:
        thousand_or_greater.append(cr[0])
print(thousand_or_greater[1:10])

highest = numerical_list[0][1]
for row in numerical_list:
    if row[1] > highest:
        highest = row[1]
        name = row[0]

print(name)


## END

