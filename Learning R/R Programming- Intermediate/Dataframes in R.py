## Int his script, we will learn about R dataframes


## Reading csv file in R

df = read.csv("recent-grads.csv")
print(df)


## Previewing the first few rows

head(df)
tail(df)

## Examining the internal structure

str(df)


## Numeric Vs. Integer

petro_eng_med_salary <- 110000
finance_med_salary <- 47000

pet_integer = is.integer(petro_eng_med_salary)
fin_integer = is.integer(finance_med_salary)


## Representing categorical values using factors

majors <- c('Arts','Biology & Life Science','Business','Computers & Mathematics', 'Engineering',
            'Health','Humanities & Liberal Arts','Psychology & Social Work','Social Science')

factor_majors <- factor(majors)
major_levels <- levels(factor_majors)


## Selecting rows

rank_1_100 <- df[1:100,]
architectural_engineering <- df[19,]
computer_science <- df[21,]


## selecting data by columns

select_df <- df[, c("Major","Unemployment_rate","Median","Men","Women")]


## Selecting specific values

mech_eng_salary <- df["MECHANICAL ENGINEERING", "Median"]
comp_sci_salary <- df["COMPUTER SCIENCE", "Median"]
finance_salary <- df["FINANCE", "Median"]


## Using comparison operators to filter values

above_50 <- df[df$Median > 50000,]
engineering <- df[df$Major_category =="Engineering", ]
great_40 <-  df[df$ShareWomen > 0.40, ]


## Combining conditional statements using logical operators

majors <- df[df$Median > 50000 & df$ShareWomen > 0.4,]


## Storing a dataframe

majors <- df[df$Median >50000 & df$ShareWomen >0.4, ]
major_choice <- majors[order(majors$Unemployment_rate),]


## 















