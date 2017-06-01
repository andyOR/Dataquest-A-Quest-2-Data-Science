# In this script, we will learn to use Pandas library. Using Pandas library over NumPy
# has many advantages. We can mixed data type, no need to manually change the missing
# values and pandas dataframes helps in working with rows and columns easily.

## Dataset used in this script include nutritional information on the most common foods Americans consume

## Read In A CSV File. Importing pandas library

import pandas

food_info = pandas.read_csv("food_info.csv")# this function is used to read file in pandas
print(type(food_info))

## Exploring The DataFrame


print(food_info.head(3)) #this will show first three rows
dimensions = food_info.shape
print(dimensions) # this show the number of rows and columns
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20) # first twenty rows

## Indexing with Pandas. pandas uses the values in the first row (also known as the header)
# for the column labels and the row number for the row labels. Collectively, the labels
## are referred to as the index

column_names = food_info.columns # to access column names


## Series object in Pandas. when you select a row from a dataframe, instead
## of just returning the values in that row as a list, pandas returns a Series object that contains
## the column labels as well as the corresponding values

## Selecting a row. Pandas uses "loc[]" method to choose row in dataset


hundredth_row = food_info.loc[99]
print(hundredth_row)

## Data types in Pandas.

print(food_info.dtypes)


## Selecting multiple rows.

print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

food_info.shape[0]
last_rows = food_info.loc[8613:8618]

## Selecting Individual Columns
## Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

print(type(ndb_col))# Display the type of the column to confirm it's a Series object.


saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## Selecting Multiple Columns By Name

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

selenium_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]

## Practice of all basics of pandas

print(food_info.columns)
print(food_info.head(2))

flist = food_info.columns.tolist() # finding column names and turning them into list
gram_columns = []
for row in flist:
    if row.endswith("(g)") is True: # finding columns with similar names or part names
        gram_columns.append(row)

gram_df = food_info[gram_columns] # list of columns with similar names
gram_df.head(3)

## END
