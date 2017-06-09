## In this script, we'll clean the data a bit more, then combine it. Finally, we'll compute correlations and perform some analysis
## We will still use the same dataset of New York city schools


## Introduction. Some datasets are not clean as we like and have duplicate DBN columns
## For example, class_size have multiple rows with same DBN number. This can create problems
## in merging the datasets.


## Condensing The Class Size Data Set

class_size = data["class_size"]
class_size = class_size[class_size["GRADE "]== "09-12"] # only data from 9-12 class
class_size = class_size[class_size["PROGRAM TYPE"]== "GEN ED"] # only data from GEN class
print(class_size.head(5))


## Computing Average Class Sizes. we will use functions  pandas.DataFrame.groupby(), agg(), and  pandas.DataFrame.reset_index()

import numpy as np


class_size = class_size.groupby("DBN").agg(numpy.mean) ## grouping on DBN values and finding mean value
class_size.reset_index(inplace = True)

data["class_size"] = class_size
print(data["class_size"])


## Condensing The Demographics Data Set

demographics = data["demographics"]
demographics = demographics[demographics["schoolyear"]== 20112012]# only subsetting the dataset for year 20112012 which provides unique DBN
data["demographics"] = demographics
print(data["demographics"].head())


## Condensing The Graduation Data Set.

graduation = data["graduation"]
graduation = graduation[graduation["Cohort"]== "2006"] # only data from 2006
graduation = graduation[graduation["Demographic"]== "Total Cohort"] # only data from demographic total cohort
data["graduation"] = graduation
print(data["graduation"].head())


## Converting AP Test Scores

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")
    
print(data["ap_2010"].head())


## Left, Right, Inner, And Outer Joins. This shows how to merge datasets on crierias of left, right, outer and inner

combined = data["sat_results"]
combined = combined.merge(data["ap_2010"], on = "DBN", how = "left") # combined ap_2010 with sat_reults on left 
combined = combined.merge(data["graduation"], on = "DBN", how = "left") # same with graduation

print(combined.head())
combined.shape

## Performing The Inner Joins

combined = combined.merge(data["class_size"], on = "DBN", how = "inner") # performing inner joins on class_size with sat_results
combined = combined.merge(data["demographics"], on = "DBN", how = "inner")
combined = combined.merge(data["survey"], on = "DBN", how = "inner")
combined = combined.merge(data["hs_directory"], on = "DBN", how = "inner")
print(combined.head())
combined.shape


## Filling In Missing Values. We will use functions  pandas.DataFrame.fillna() and  pandas.DataFrame.mean() here

means = combined.mean()

combined = combined.fillna(means) # columns filled with mean of the column
combined = combined.fillna(0) # rest are filled with zeros
print(combined.head())
combined.shape


## Adding A School District Column For Mapping
                        
def ext(cols):
    return cols[0:2]
    

combined["school_dist"] = combined["DBN"].apply(ext)
print(combined["school_dist"].head())



##Along the way, we've learned about:

#How to handle missing values
#Different types of merges
#How to condense data sets
#How to compute averages across dataframes

## END
