## In this script, we'll explore how to create indexes for speeding up queries that filter on multiple columns

## Introduction

import sqlite3
conn = sqlite3.connect("factbook.db")

query_plan_one = conn.execute("Explain query plan select * from facts where population > 1000000 and population_growth > 0.05;").fetchall()
print(query_plan_one)


## Query Plan For Multi-Column Queries

conn = sqlite3.connect("factbook.db")

conn.execute("Create Index if not exists pop_idx on facts(population);")
conn.execute("Create Index if not exists pop_growth_idx on facts(population_growth);")
query_plan_two = conn.execute("Explain query plan select * from facts where population > 1000000 and population_growth > 0.05;").fetchall()
print(query_plan_two)


## Explanation


## Multi-Column Index


## Creating A Multi-Column Index

conn = sqlite3.connect("factbook.db")

conn.execute("CREATE INDEX if not exists pop_pop_growth_idx ON facts(population, population_growth);")
query_plan_three = conn.execute("Explain query plan select * from facts where population > 1000000 and population_growth > 0.05;").fetchall()
print(query_plan_three)


## Covering Index

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_four = conn.execute("explain query plan select population, population_growth from facts where population > 1000000 and population_growth > 0.05;").fetchall()
print(query_plan_four)


## Covering Index For Single Column

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_five = conn.execute("explain query plan select population from facts where population > 1000000;").fetchall()
print(query_plan_five)

