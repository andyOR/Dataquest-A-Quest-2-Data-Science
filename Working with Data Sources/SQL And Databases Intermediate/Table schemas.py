## In this script, we will learn to use table schemas
## Table schemas let us create new tables to store data. What we store may change over time, so SQL also allows us to modify the schema of a table over time
## This definition, which contains information like column names, data types, and which column is the primary key, is called a table schema
##  SQL databases are commonly known as relational databases because they support relations between tables


## Adding Columns

ALTER TABLE facts
ADD leader text;

# When you add a column, all the values associated with it will be NULL to begin with


## Removing Columns

ALTER TABLE facts
DROP COLUMN awesomeness;


## Creating Tables

CREATE TABLE factbook.leaders(
   id integer PRIMARY KEY,
   name text,
   country text
);


## Relations Between Tables

CREATE TABLE factbook.leaders(
   id integer PRIMARY KEY,
   name text,
   country integer,
   worth float,
   FOREIGN KEY(country) REFERENCES facts(id)
);


## Creating A Table With Relations

CREATE TABLE factbook.states(
    id integer PRIMARY KEY,
    name text,
    area integer,
    country integer,
    FOREIGN KEY(country) REFERENCES facts(id)


## Querying Across Foreign Keys

select * from landmarks
INNER JOIN facts
ON landmarks.country==facts.id;


## Types Of Joins

# INNER JOIN is the most common type of join, but LEFT OUTER JOIN is also occassionally used. It's very uncommon to use RIGHT OUTER JOIN, and SQLite doesn't support it
# From a syntax points of view, using the statements is the exact same, you just swap out INNER JOIN for LEFT OUTER JOIN

## Types Of Joins

select * from landmarks
LEFT OUTER JOIN facts
ON landmarks.country==facts.id;


## END
);
