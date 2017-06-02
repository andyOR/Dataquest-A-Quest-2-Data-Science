## In this script, we will perform data manipulation with Pandas.

##Introduction or Overview

import pandas
food_info = pandas.read_csv("food_info.csv")
col_names= food_info.columns.tolist()# finding columns names
print(col_names)

## Transforming a column

div_1000 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2
sodium_grams = food_info["Sodium_(mg)"] / 1000 # transforming sodium column from mg to gm and forming a series
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

## Performing Math With Multiple Columns

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] /food_info["Water_(g)"]# dividing columns
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]# Adding

## creating a nutritional Index

weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = food_info["Lipid_Tot_(g)"] * -0.75
initial_rating = weighted_protein + weighted_fat

## Normalizing Columns In A Data Set

print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()

max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / max_protein

max_Lipid = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_Lipid

## Creating A New Column

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

## Create A Normalized Nutritional Index

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

food_info["Norm_Nutr_Index"] = 2 * food_info["Normalized_Protein"] - 0.75 * food_info["Normalized_Fat"]

## Sorting dataset by column value

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])
food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)




