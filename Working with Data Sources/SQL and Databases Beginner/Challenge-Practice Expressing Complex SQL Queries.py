## In this challenge, we'll practice writing your own SQL queries from scratch


## Use SELECT And LIMIT To Filter Results

select College_jobs,Median,Unemployment_rate
from recent_grads
limit 20;


## Use WHERE To Filter Results

select Major
from recent_grads
where Major_category = "Arts"
limit 5;


## Express Criteria With Operators

select Major, Total, Median, Unemployment_rate
from recent_grads
where (Major_category != "Engineering") and (Median <= 50000 or Unemployment_rate >= 0.065);


## Order Your Results

select Major
from recent_grads
where Major_category !="Engineering"
order by Major desc
limit 20;


## END
