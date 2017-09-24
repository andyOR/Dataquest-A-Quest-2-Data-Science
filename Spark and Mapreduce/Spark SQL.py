## In this mission, we'll learn how to use Spark's SQL interface to query and interact with the data.

## We'll continue to work with the 2010 U.S. Census data set in this mission.


## Register dataframe as a Table

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)


## Querying

ag = sqlCtx.sql('select age from census2010')
ag.show()

query = 'select males females from census2010 where age > 5 and age < 15'

## Mixing functionality

ag = sqlCtx.sql('select males females from census2010')
ag.describe().show()


## Multiple Tables

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
df = sqlCtx.read.json("census_1980.json")
df.registerTempTable('census1980')
df = sqlCtx.read.json("census_1990.json")
df.registerTempTable('census1990')
df = sqlCtx.read.json("census_2000.json")
df.registerTempTable('census2000')
tables = sqlCtx.tableNames()
print(tables)


## Joins in SparkSQL

query = """
 select census2010.total, census2000.total
 from census2010
 inner join census2000
 on census2010.age=census2000.age
"""

sqlCtx.sql(query).show()


## SQLFunctions

query = '''
select sum(census2010.total), sum(census2000.total), sum(census1990.total)
from census2010
inner join census2000
on census2010.age=census2000.age
inner join census1990
on census2010.age=census1990.age
'''
sqlCtx.sql(query).show()


## END
