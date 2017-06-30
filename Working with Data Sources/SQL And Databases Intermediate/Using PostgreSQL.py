## In this mission, we'll look at the basics of PostgreSQL, then dive into creating a database, querying data, and some advanced features



## SQLite Vs PostgreSQL

## In general, SQLite is good in cases where having a small and simple database engine is important.
## SQLite is used extensively in embedded applications, such as Android and iOS applications
## In cases where there will be multiple users or performance is important, PostgreSQL is the most commonly used database engine.
## PostgreSQL is open source, and is free to download and use


## PostgreSQL Overview

# The most common Python client for PostgreSQL is called psycopg2

import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres")# need to specify which user we're connecting as, and which database we're connecting to
cur = conn.cursor()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname = dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()


## Creating A Table

import psycopg2
conn = psycopg2.connect("dbname = dq user=dq")
cur = conn.cursor()
query = '''
create table notes(
id integer PRIMARY KEY,
body text,
title text);
'''
cur.execute(query)
conn.close()


## SQL Transactions

import psycopg2
conn = psycopg2.connect("dbname = dq user=dq")
cur = conn.cursor()
query = '''
create table notes(
id integer PRIMARY KEY,
body text,
title text);
'''
cur.execute(query)
conn.commit()# commiting changes
conn.close()


## Autocommitting

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value integer)")
conn.close()


## Executing Queries

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute('select * from notes;')
print(cur.fetchall())
conn.close()


## Creating A Database

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('CREATE DATABASE income OWNER dq;')
conn.close()


## Deleting A Database

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('DROP DATABASE income;')
conn.close()


## END























