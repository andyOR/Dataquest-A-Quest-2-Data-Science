## In this script, In this mission, we'll explore how to express more complex filtering criteria in SQL



## Introduction To Logical Operators

# Logical operators are keywords we can use to combine filtering criteria and express more specific conditions. Here are the two basic logical operators we use most often:

# OR (returns either Condition1 or Condition2)
# AND (returns both Condition1 and Condition2)


## Returning Multiple Conditions With AND

SELECT Major,ShareWomen,Employed 
FROM recent_grads 
WHERE ShareWomen>0.5 AND Employed>10000
Limit 10;


## Returning One Of Several Conditions With OR

SELECT Major,Median,Unemployed
FROM recent_grads
Where Median >=10000 or Unemployed <= 1000
Limit 20;


## Grouping Operators With Parentheses

select Major,Major_category, ShareWomen,Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);


## Practice Grouping Operators

select Major,Major_category, Employed,Unemployment_rate
from recent_grads
where (Major_category = 'Business' or Major_category='Arts' or Major_category='Health' ) and (Employed >20000 or Unemployment_rate < 0.051);



## Order Results With ORDER BY

select Major
from recent_grads
order by Major desc
limit 10;


## Order Results Based On Multiple Columns

select Major_category, Median, Major
from recent_grads
order by Major asc, Median desc
limit 20;


## END












