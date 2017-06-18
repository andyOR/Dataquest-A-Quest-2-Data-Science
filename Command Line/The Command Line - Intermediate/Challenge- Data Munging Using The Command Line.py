## In this script, we'll practice the command line concepts learned so far by munging datasets using just the command line.
##  Data munging involves transforming datasets to make them easier to work with


## Data Exploration

head -n 10 Hud_csv2005.csv Hud_2007.csv Hud_2013.csv # displays first 10 rows for all three files


## Filtering

head -1 Hud_2005.csv > combined_hud.csv # taking header row from file and adding to new file

wc -l Hud_2005.csv # gives total number of rows in file

tail -46853 Hud_2005.csv >> combined_hud.csv # adding nonheader rows from one file to common file


## Consolidating Datasets

#adding other datasets to combined_hud.csv

tail -42729 Hud_2007.csv >> combined_hud.csv                          
tail -64535 Hud_2013.csv >> combined_hud.csv


## Counting

grep "1980-1989" combined_hud.csv | wc -l


## END
