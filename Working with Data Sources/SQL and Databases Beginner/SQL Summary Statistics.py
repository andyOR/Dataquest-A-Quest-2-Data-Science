## In this script, we'll learn how to count with SQL only


## Introduction

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "select * from facts;"
facts = conn.execute(query).fetchall()
print(facts)
facts_count = len(facts)

## Counting The Number Of Rows In SQL

conn = sqlite3.connect("factbook.db")

query = "select COUNT(birth_rate) from facts;"
birth = conn.execute(query).fetchall()
birth_rate_count = birth[0]
print(birth_rate_count)


## Finding A Column's Minimum And Maximum Values In SQL

conn = sqlite3.connect("factbook.db")

query = "select MIN(population_growth) from facts;"
min_pop = conn.execute(query).fetchall()
min_population_growth = min_pop[0]
print(min_population_growth)

query1 = "select MAX(death_rate) from facts;"
max_dt = conn.execute(query1).fetchall()
max_death_rate = max_dt[0]
print(max_death_rate)


## Calculating Sums And Averages In SQL

conn = sqlite3.connect("factbook.db")

query = "select SUM(area_land) from facts;"
total_land = conn.execute(query).fetchall()
total_land_area = total_land[0]
print(total_land_area)

query1 = "select AVG(area_water) from facts;"
area_water = conn.execute(query1).fetchall()
avg_water_area = area_water[0]
print(avg_water_area)


## Combining Multiple Aggregation Functions

conn = sqlite3.connect("factbook.db")

query = "SELECT AVG(population), SUM(population), MAX(birth_rate) from facts;" 
facts_stats = conn.execute(query).fetchall()
print(facts_stats)


## Aggregating Values For A Subset Of The Data

conn = sqlite3.connect("factbook.db")

query = "SELECT AVG(population_growth) FROM facts WHERE population > 10000000;"
population_growth = conn.execute(query).fetchall()
population_growth = population_growth[0]
print(population_growth)


## Selecting Unique Rows

conn = sqlite3.connect("factbook.db")

query = "SELECT DISTINCT birth_rate from facts;"
unique_birth_rates = conn.execute(query).fetchall()

print(unique_birth_rates)


## Performing Arithmetic Between Columns

conn = sqlite3.connect("factbook.db")

query = "select (1+(population_growth/100)) * population from facts;"
next_year_population = conn.execute(query).fetchall()
print(next_year_population)


## END


## Aggregating Unique Values

conn = sqlite3.connect("factbook.db")

query = "SELECT AVG(DISTINCT birth_rate) from facts where population > 20000000;"
unique_birth_rates = conn.execute(query).fetchall()
average_birth_rate = unique_birth_rates[0]

print(average_birth_rate)

query1 = "SELECT SUM(DISTINCT population) from facts where area_land > 1000000;"
a = conn.execute(query1).fetchall()
sum_population = a[0]

print(sum_population)

## Performing Arithmetic In SQL

conn = sqlite3.connect("factbook.db")

query = "select population_growth/1000000.0 from facts;"
population_growth_millions = conn.execute(query).fetchall()
print(population_growth_millions)


## 












































