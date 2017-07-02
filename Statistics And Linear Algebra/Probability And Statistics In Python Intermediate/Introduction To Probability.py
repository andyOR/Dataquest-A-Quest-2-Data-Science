## In this script, we will cover the basics of probability.

## We will use the datasets "flags.csv" containing information on flags of countries around the world
## This data was collected from Collins Gem Guide to Flags


## Probability Basics

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags["name"][flags["bars"].idxmax()]
highest_population_country = flags["name"][flags["population"].idxmax()]


## Calculating Probability

total_countries = flags.shape[0]
country_col_orange = flags["name"][flags["orange"] == 1]
orange_probability = len(country_col_orange)/total_countries

country_num_stripe = flags["name"][flags["stripes"] > 1]
stripe_probability = len(country_num_stripe)/total_countries


## Conjunctive Probabilities

five_heads = .5 ** 5

ten_heads = .5 ** 10

hundred_heads = .5 ** 100


## Dependent Probabilities

