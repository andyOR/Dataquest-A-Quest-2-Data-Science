## In this script, we'll explore how to interact with a SQLite database in Python so you can start to incorporate databases into your data science workflow


## We can interact with a SQLite database in two main ways:

# Through the SQLite Python module
# Through the SQLite shell

# Connecting To The Database

import sqlite3
conn = sqlite3.connect("jobs.db")


## Introduction To Cursor Objects And Tuples


## Working With Sequences Of Values As Tuples

# A tuple is a core data structure that Python uses to represent a sequence of values, similar to a list.
# Unlike lists, tuples are immutable, which means we can't modify existing ones.
# Python represents each row in the results set as a tuple


## Creating A Cursor And Running A Query

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:2])


## Execute As A Shortcut For Running A Query

conn = sqlite3.connect("jobs.db")
query = "select * from recent_grads;"
conn.execute(query).fetchall()


## Fetching A Specific Number Of Results

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "Select Major, Major_category from recent_grads";
five_results = conn.execute(query).fetchmany(5)


## Closing The Database Connection

conn = sqlite3.connect("jobs.db")
conn.close()


## Practice

import sqlite3
conn = sqlite3.connect("jobs2.db")

query = "select Major from recent_grads order by major desc";
reverse_alphabetical = conn.execute(query).fetchall()
conn.close()


## END




















