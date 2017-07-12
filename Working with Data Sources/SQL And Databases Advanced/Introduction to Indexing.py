## In this script, we'll explore how queries are executed in SQLite.
## After exploring this at a high level, we explore how to create and use indexes for better performance


## Introduction

import sqlite3
conn = sqlite3.connect("factbook.db")

query = 'PRAGMA table_info(facts);'
schema = conn.execute(query).fetchall()
for i in schema:
    print(i)


## Query Planner

# When you execute a SQL query, SQLite performs many steps before returning the results to you
# The query optimizer generates cost estimates for the various ways to access the underlying data, factoring in the schema of the tables and the operations the query requires
# The optimizer quickly assesses the various ways to access the data and generates a best guess for the fastest query plan


## Explain Query Plan

query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts where area > 40000;").fetchall()
print(query_plan_one)

query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT area FROM facts where area > 4000;").fetchall()
print(query_plan_two)

query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts where name = 'Czech Republic';").fetchall()
print(query_plan_three)


## Data Representation


## Time Complexity

query_plan_four = conn.execute("Explain query plan SELECT * FROM facts WHERE id=20;").fetchall()# using row id
print(query_plan_four)


## Search And Rowid


## Indexing


## Create An Index


## All together

query_plan_six = conn.execute("Explain query plan select * from facts where population > 10000;").fetchall()
print(query_plan_six)

conn.execute("CREATE INDEX IF NOT EXISTS pop_idx ON facts(population);")
query_plan_seven = conn.execute("Explain query plan select * from facts where population > 10000;").fetchall()
print(query_plan_seven)



## END
