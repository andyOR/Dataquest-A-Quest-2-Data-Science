## In this script, we'll learn how to work with files and use loops to iterate through lists
## We'll be working with crime rate data for 73 cities in the United States


## Opening Files

a = open("test.txt", "r") # name of the file and mode of working with the file
print(a)
f = open("crime_rates.csv", "r")


## Reading In Files. File objects have a read() method that returns a string representation of the text in a file

f = open("crime_rates.csv", "r")
data = f.read()


## Splitting. The split() method takes a string input corresponding to the delimiter, or separator

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n') #data split on new line character "\n"
print(rows[0:5])


## Loops. Writing a for loop on a subset of the crime rate data.

ten_rows = rows[0:10]
for rate in ten_rows:
    print(rate)


## List Of Lists.

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])


## Practice - Splitting Elements In A List

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []

for element in rows:
    g = element.split(',')
    final_data.append(g)
print(final_data[0:5])


## Accessing Elements In A List Of Lists: The Manual Way

print(five_elements)
cities_list = []

for i in five_elements:
    g = i[0]
    cities_list.append(g)
print(cities_list)


## Looping Through A List Of Lists

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = []
for i in final_data:
    g = i[0]
    cities_list.append(g)


## Challenge

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []
for i in rows:
    g = i.split(',')
    h = int(g[1])
    int_crime_rates.append(h)
    
print(int_crime_rates)


## END


