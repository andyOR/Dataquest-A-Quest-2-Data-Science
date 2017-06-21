## In this script, we'll be focusing on a language called SQL, or Structured Query Language. We use SQL to query, update, and modify the data in a database
## SQL is the most common language for working with databases, and an important tool in any data professional's toolkit


## Understanding Tables, Rows, And Columns

# A database is a collection of tables. Each table is made up of rows of data, and each row has values for the same set of columns
# We'll be working with the data from the American Community Survey on college majors and job outcomes "recent-grads.csv"


## Querying Databases With SQL

# We use a SELECT statement whenever we want to return specific data from the database without editing or modifying it
# The semicolon (;) at the end of the query is required because it specifies where the query ends


## Querying A SQLite Database

SELECT Rank,Major # selecting columns of rank and major
FROM recent_grads;


## Specifying Column Order For Our Results

SELECT Major,Rank
FROM recent_grads;


## Practice: Selecting Columns With SELECT

SELECT Rank, Major_code, Major, Major_category, Total
FROM recent_grads;


## Filtering With The WHERE Statement
# most database systems require that the SELECT and FROM statements come first, before any WHERE or other statements

SELECT Major, ShareWomen
FROM recent_grads
Where ShareWomen > 0.5;


## Practice: Filtering With WHERE Statements

SELECT Major, Employed
FROM recent_grads
Where Employed > 10000;


## Limiting The Number Of Results

SELECT Major
FROM recent_grads 
Where Employed > 10000
LIMIT 10;# this limits to first 10 rows in result


## END





