## In this mission, we'll explore how to calculate more granular summary statistics in SQL

## We'll be working with a data set on jobs we stored in the recent_grads table of jobs.db


## Introduction

select * from recent_grads
limit 5;



## Calculating Group-Level Summary Statistics

select Major_category, AVG(ShareWomen)
from recent_grads
group by Major_Category;


## Renaming Columns With The AS Statement

select SUM(Men) AS total_men, SUM(Women) AS total_women
from recent_grads;


## Practice: Using GROUP BY

select Major_category, AVG(Employed) / AVG(Total) as share_employed
from recent_grads
group by Major_category;


## Querying Virtual Columns With The HAVING Statement

SELECT Major_category, AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
from recent_grads
group by Major_category
Having share_low_wage > 0.1;


## Rounding Results With The ROUND Function

select ROUND(ShareWomen, 4), Major_category
from recent_grads
limit 10;


## Nesting Functions

select Major_category, ROUND(AVG(College_jobs) / AVG(Total),3) as share_degree_jobs
from recent_grads
group by Major_category
Having share_degree_jobs < 0.3;


## END

