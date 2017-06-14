## in this script, we will perform data analysis on "thanksgiving.csv" data, survey of thanksgiving data
## It contains 65 columns and 1058 rows or responses
## The dataset came from FiveThirtyEight, and can be found at https://github.com/fivethirtyeight/data/tree/master/thanksgiving-2015


## Reading the dataset and information on columns

import pandas as pd
data = pd.read_csv("thanksgiving.csv",encoding="Latin-1" )
print(data.head())

data.columns


## Filtering Out Rows From A DataFrame. The column Do you celebrate Thanksgiving? contains information of ppl celebrated thanksgiving.
## We only want to keep data for people who answered Yes to this questions.

celeb_counts = data["Do you celebrate Thanksgiving?"]
celeb_counts.value_counts()

data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


## Using Value_counts To Explore Main Dishes

celeb_dish = data["What is typically the main dish at your Thanksgiving dinner?"]
celeb_dish.value_counts()

celeb_tofurkey = data[data["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"]
celeb_gravy = celeb_tofurkey["Do you typically have gravy?"]
print(celeb_gravy)


## Figuring Out What Pies People Eat

apple = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"]
apple_isnull = pd.isnull(apple)
pumpkin = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"]
pumpkin_isnull = pd.isnull(pumpkin)
pecan = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"]
pecan_isnull = pd.isnull(pecan)

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies_unique = ate_pies.value_counts()
print(ate_pies_unique)


## Converting Age To Numeric

data["Age"].value_counts()

def age_count(age_str):
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(" ")[0]
    age_str = age_str.replace("+", "")
    return int(age_str)
    
data["int_age"] = data["Age"].apply(age_count)
print(data["int_age"].describe())


## Converting Age To Numeric

data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts()

def earn_count(earnings):
    if pd.isnull(earnings):
        return None
    earnings = earnings.split(" ")[0]
    if earnings == "Prefer":
        return None
    earnings = earnings.replace("$", "")
    earnings = earnings.replace(",", "")
    return int(earnings)


## Correlating Travel Distance And Income

less_income = data[data["int_income"] < 150000]
less_income = less_income["How far will you travel for Thanksgiving?"]
print(less_income.value_counts())

less_income = data[data["int_income"] < 150000]
less_income = less_income["How far will you travel for Thanksgiving?"]
print(less_income.value_counts())
data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(earn_count)
print(data["int_income"].describe())


## Linking Friendship And Age

data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?",
                       columns = 'Have you ever attended a "Friendsgiving?"', 
                       values = "int_age")

data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


##
