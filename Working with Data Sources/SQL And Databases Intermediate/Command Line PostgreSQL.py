##  In this script, we'll learn how to work with the PostgreSQL command line tool, called psql


## The Psql Tool

psql # starting postgresql at command line
\q # exit


## Running SQL Queries

pqsl
Create database bank_accounts;
\q


## Special PostgreSQL Commands

# We can run several special commands using psql

# Two common functions to run are:

\l #-- list all available databases.
\dt #-- list all tables in the current database.
\du #-- list users.


## Switching Databases

pqsl -d bank_accounts # starting database bank_accounts
create table deposits(id integer primary key, name text, amount 
float);
\dt
\q


## Creating Users

pqsl
create role sec with createdb login password 'test';# creating username
\du
\q


## Adding Permissions

pqsl -d bank_accounts
grant all privileges on deposits to sec;
\dp deposits # checking permission to users
\q


## Removing Permissions

pqsl -d bank_accounts
revoke all privileges on deposits from sec;
\dp deposits # checking permission to users
\q


## Superusers

create role aig with login password 'test' superuser;



## END



