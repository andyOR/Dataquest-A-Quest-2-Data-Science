## In this script, we will learn about lists in R

## Reviewing our data structures

companies <- list("boom_tech","car_mechanics","Pineapple.co","slurp_snacks")


## Creating a list of objects

research <- list("Data Analyst", c(74000,60000,80000), "Must have skills with R programming")


## Naming of your list

research <- list("Data Analyst", c(74000,60000,80000), "Must have skills with R programming")

named_research <- c("job_title","salaries","job_requirements")

names(research) <- named_research


## Creating a Named list

research <- list(job_title = "Data Analyst",
                 salaries = c(74000,60000,80000),
                 job_requirements = "Must have skills with R programming")


## Adding values to list

research <- list(job_title = "Data Analyst", salaries = c(74000,60000,80000), job_requirements = "Must have skills with R programming")

research <- c(research, Vacation: 21)


## Indexing a list

research <- list(job_title = "Data Analyst", salaries = c(74000,60000,80000), job_requirements = "Must have skills with R programming")

salaries = research$salaries


## Changing values in a list

research <- list(job_title = "Data Analyst", salaries = c(74000,60000,80000), job_requirements = "Must have skills with R programming")

research[[1]] <- "Jr. Data Scientist"


## Merging lists

research <- list(job_title = "Jr. Data Scientist", salaries = c(74000,60000,80000), job_requirements = "Must have skills with R programming", vacation = 28)

more_research <- list(retirement = "pension", bonus = 10000, commute_time = "30 minutes")

combined <- c(research, more_research)












