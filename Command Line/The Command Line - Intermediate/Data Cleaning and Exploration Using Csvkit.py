## In this script, we'll learn about the Csvkit library, which supercharges your workflow
## by adding 13 new command line tools specifically for working with CSV files
## We'll focus on these 5 tools from Csvkit

## Csvstack

csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.
csv > Combined_hud.csv
# n for new row for file unique row, -g for making a new row with unique value rows

head Combined_hud.csv

wc -l Combined_hud.csv


## Csvlook. The csvlook tool parses CSV formatted data from it's stdin and
# outputs a pretty formatted table representation of that data to it's stdout

head -10 Combined_hud.csv | csvlook


## Csvcut

csvcut -n Combined_hud.csv

csvcut -c 2 Combined_hud.csv | head -10


## Csvstat

# Just the max value.
csvcut -c 2 Combined_hud.csv | csvstat --max
# Just the mean value.
csvcut -c 2 Combined_hud.csv | csvstat --mean
# Just the number of null values.
csvcut -c 2 Combined_hud.csv | csvstat --nulls

csvcut Combined_hud.csv | csvstat --mean# mean of all columns


## Csvcut | Csvstat

csvcut -c 2 Combined_hud.csv | csvstat


# Csvgrep. Displaying first 10 rows from Combined_hud.csv where the value for the AGE1 column is -9 in a pretty table format

csvgrep -c 2 -m -9 Combined_hud.csv | head -10 | csvlook 


## Filtering Out Problematic Rows

csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv # all rows where the value for AGE1 isn't -9 and writing just those rows to positive_ages_only.csv#


## END
