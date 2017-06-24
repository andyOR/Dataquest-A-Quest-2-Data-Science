##  CIA World Factbook, a compendium of facts about countries.
# The Factbook contains demographic information for each country in the world


## Overview Of The SQLite Command Shell

sqlite3 factbook.db
.help
.tables


## Running Queries In The SQLite Command Shell

SELECT * FROM facts ORDER BY population DESC LIMIT 10;
SELECT * FROM facts ORDER BY area_land ASC LIMIT 10;


## Using Python With SQLite

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "select name, population from facts order by population";
print(conn.execute(query).fetchmany(10))


## Using Python With SQLite

import pandas as pd
import sqlite3
import math
conn = sqlite3.connect('factbook.db')

a = pd.read_sql_query('SELECT * FROM facts;', con = conn )
a = a.dropna(axis = 0)
a = a[(a['area_land'] > 0) & (a['population'] > 0)]

def pop_grow(x):
    return x['population'] * math.e ** ((x['population_growth']/100) *35)
    
a['pop_2050'] = a.apply(lambda row: pop_grow(row), axis = 1)
b = a.sort(['pop_2050'], ascending = [False])
b = b['name'].iloc[0:9]
print(b)


## Summing Columns To Compute Total Area

import pandas as pd
import sqlite3
import math
conn = sqlite3.connect('factbook.db')

area1 = pd.read_sql_query('SELECT SUM(area_land), SUM(area_water) FROM facts where area_land !="";', con = conn )

print(area1['SUM(area_land)']/area1['SUM(area_water)'])


## My Addition- High density regions

import pandas as pd
import sqlite3
import math
conn = sqlite3.connect('factbook.db')

densit = pd.read_sql_query('SELECT name, population, area_land FROM facts where area_land !="" order by population desc;', con = conn )
a = densit.dropna(axis = 0)
densit = a[(a['area_land'] > 0) & (a['population'] > 0)]

densit["high_densit"] = densit['population']/densit['area_land']
hdensit= densit.sort(["high_densit"], ascending = [False])
print(hdensit.head(20))
#high_densit = 
#column = densit["population", "high_densit"]
#print(column.head())


## END
