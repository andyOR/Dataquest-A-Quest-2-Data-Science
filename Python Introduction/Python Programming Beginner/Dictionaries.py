## In this script, we will learn concepts of "Dictionaries" in python.
## A dictionary is like a list in that it has indexes, but the indexes aren't necessarily sequential numbers.
## We can create our own indexes with values of any data type, including strings
## We will use the LA weather data

## The Data Set

# Weather has been loaded in.
print(weather[0])
g = len(weather)
print(weather[g-1])


## Dictionaries

scores = {}
scores["Tom"] = 70
scores["Jim"] = 80
scores["Sue"] = 85
scores["Ann"] = 75
# Taken together, we call the index and value key/value pairs. A dictionary key can be a string, integer, or float


## Practice Populating A Dictionary

superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2


## Practice Indexing A Dictionary.

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

## Defining A Dictionary With Values

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
animals = {
    7:"raven",
    8:"goose",
    9:"duck" 
}
times = {
    "morning": 9,
    "afternoon":14,
    "evening":19,
    "night":23
}


## Modifying Dictionary Values

students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5


## The In Statement And Dictionaries

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers


## The Else Statement

if temperature > 50:
    print("It's hot!")
else:
    print("It's cold!")


## Practicing With The Else Statement

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for i in planet_names:
    p = len(i)
    if p > 5:
        long_names.append(i)
    else:
        short_names.append(i)


## Counting With Dictionaries

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for p in pantry:
    if p in pantry_counts: 
        pantry_counts[p] = pantry_counts[p] + 1
    else:
        pantry_counts[p] = 1


## Counting The Weather

weather_counts = {}
for i in weather:
    if i in weather_counts:
        weather_counts[i] = weather_counts[i] + 1
    else:
        weather_counts[i] = 1


## END

