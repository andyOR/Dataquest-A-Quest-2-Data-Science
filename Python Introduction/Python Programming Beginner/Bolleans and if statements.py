## In this scripts, we will learn to use booleans and if statements


## Booleans.

#Python has a class called Boolean that helps express conditional logic.
#There are only two Boolean values: True and False

cat = True
dog = False
print(type(cat))# display 'bool' type

print(cities)
first_alb = (cities[0] == "Albuquerque")
second_alb = (cities[1] == "Albuquerque")
g = len(cities)
first_last = (cities[0] == cities[g-1]) # gives False output

## Booleans with "Greater than" and "less than"
print(crime_rates)
first_500 = (crime_rates[0] > 500)
first_749 = (crime_rates[0] >= 749)
g = len(crime_rates)
first_last = (crime_rates[0]>=crime_rates[g-1])


print(crime_rates)
second_500 = (crime_rates[1] <500)
second_371 = (crime_rates[1] <= 371)
g = len(crime_rates)
second_last = (crime_rates[1] <= crime_rates[g-1])


## If Statements. To complement Booleans, Python contains the if operator

result = 0
if (cities[2] == "Anchorage"):
    result = 1


## Nesting If Statements

both_conditions = False
if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        both_conditions = True


## If Statements And For Loops

five_hundred_list =[]
for cr in crime_rates:
    if cr > 500:
        five_hundred_list.append(cr)


## Find The Highest Crime Rate

print(crime_rates)
highest = crime_rates[0]
for cr in crime_rates:
    if cr > highest:
        highest = cr


## END





