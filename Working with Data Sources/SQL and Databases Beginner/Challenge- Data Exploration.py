## In this challenge, we'll practice calculating summary statistics in SQL while exploring data from factbook.db


## Introduction

conn = sqlite3.connect("factbook.db")

query = "select AVG(population), AVG(population_growth), AVG(birth_rate), AVG(death_rate) from facts;"
result = conn.execute(query).fetchall()
pop_avg = result[0]
pop_growth_avg = result[0][1]
birth_rate_avg = result[0][2]
death_rate_avg = result[0][3]


## Find Ranges

conn = sqlite3.connect("factbook.db")

averages = "select MIN(population), MAX(population), MIN(population_growth), MAX(population_growth),  MIN(birth_rate),  MAX(birth_rate), MIN(death_rate), MAX(death_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_min = avg_results[0][0]
pop_max = avg_results[0][1]
pop_growth_min = avg_results[0][2]
pop_growth_max = avg_results[0][3]
birth_rate_min = avg_results[0][4]
birth_rate_max = avg_results[0][5]
death_rate_min = avg_results[0][6]
death_rate_max = avg_results[0][7]


## Filter Values

conn = sqlite3.connect("factbook.db")

conn = sqlite3.connect("factbook.db")

averages = "select MIN(population), MAX(population), MIN(population_growth), MAX(population_growth),  MIN(birth_rate),  MAX(birth_rate), MIN(death_rate), MAX(death_rate) from facts where population < 2000000000 and population > 0;"
avg_results = conn.execute(averages).fetchall()
pop_min = avg_results[0][0]
pop_max = avg_results[0][1]
pop_growth_min = avg_results[0][2]
pop_growth_max = avg_results[0][3]
birth_rate_min = avg_results[0][4]
birth_rate_max = avg_results[0][5]
death_rate_min = avg_results[0][6]
death_rate_max = avg_results[0][7]


## Predict Future Population Growth

import sqlite3
conn = sqlite3.connect("factbook.db")
projected_population_query = '''
select round(population + population * (population_growth/100), 0) from facts
where population > 0 and population < 7000000000 
and population is not null and population_growth is not null;
'''

projected_population = conn.execute(projected_population_query).fetchall()

print(projected_population[0:10])


## Explore Projected Population

import sqlite3
conn = sqlite3.connect("factbook.db")
proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)


## END
