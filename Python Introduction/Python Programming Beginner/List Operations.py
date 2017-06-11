## In this scripts, we will look at list operations in Python
## "la_weather.csv" contains daily weather data for Los Angeles (L.A.) during 2014


## Introduction to the data and Pasing the file

weather_data = []
f = open("la_weather.csv",'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row) # created a list of list
print(weather_data[0:4])

## Getting A Single Column From The Data

weather = []
for row in weather_data:
    r = row[1]
    weather.append(r)


## Counting The Items In A List

count = 0

for r in weather:
    count = count + 1


## Removing The Header

new_weather = weather[1:366]


## The In Statement

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals # False output


## Weather Types

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for cr in weather_types:
    result = cr in new_weather # boolean checks if weather types are present in our weather data
    weather_type_found.append(result)


## In this mission, we covered list slicing, columns, and the in statement


## 
    
