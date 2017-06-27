## In this script, we will learn to modify databases in SQL using three statements of
## INSERT, UPDATE, and DELETE

## we'll be working with factbook.db, a SQLite database that contains information about each country in the world.


## Working With Dates In SQL

select *
from facts
where created_at < "2015-11-01 15:00" and created_at > "2015-10-30 16:00";


## Data Types

PRAGMA table_info(facts);


## Primary Keys

select *
from facts
order by id desc
Limit 1;


## Inserting Data Into A Table

insert into facts
values (262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");


## Missing Values

SELECT * FROM facts 
WHERE area IS NULL;

insert into facts
values (263, "dq", "DataquestLand", NULL, NULL, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00")


## Updating Rows

update facts
set name = "United States"
where name = "DataquestLand";


## Deleting Rows

delete from facts
where name="Canada";


## END



























"2016-02-25 12:00:00", "2016-02-25 12:00:00");
