## In this script, we are starting data cleaning techniques and how to acquire
## raw data. This will help us to clean messy data into clean datasets


## In this script, we will be using data about New York city public schools
## https://data.cityofnewyork.us/browse?category=Education

## Finding All Of The Relevant Data Sets. We will analyzing SAT scores and relevant
## demographic information to make correlation. To do this many other datasets needs to be
## consider and merge to form our complete dataset


## Finding Background Information. Background research will give us a better understanding of how to combine and analyze the data


## Reading In The Data

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {} # dictionary

for row in data_files:
    read = pd.read_csv("schools/{0}".format(row))## reading the path and file as well
    keys = row.replace(".csv", "")# changing the file name
    data[keys] = read # dictionary with dataframe as key variables


## Exploring the SAT Data

sat = data['sat_results']
print(sat.head(5))


## Exploring The Remaining Data

for row in data:
    score = data[row]
    print(score.head(5))## five rows of every dataframe in dic. data



## Reading In The Survey Data. Looking for coomon rows to merge all datasets (DBN's)
## we need to check for duplicate DBN'd before merging


## another function called  pandas.concat() function for combining two dataframes by columns.

z = pd.concat([x,y], axis=0) # The combined dataframe z will have the number of rows in x plus the number of rows in y


## Reading In The Survey Data

all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")## check the delimiter to txt files

survey = pd.concat([all_survey, d75_survey], axis = 0)
print(survey.head(5))


## Cleaning Up The Surveys. Extracting the columns we need and taking out others

survey["DBN"] = survey["dbn"] # changing column name to uppercase for matching with other datasets

fields = ["DBN","rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey = survey.loc[:,fields]
data['survey'] = survey
print(survey.head(5))


## Inserting DBN Fields. Some dataframes does not include DBN but combination of it

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def add_num(cols):
   number = str(cols)
   if len(number) > 2:
       return number
   else:
       return number.zfill(2)
        
        #padded_csd.append(number)
    #cols["padded_csd"] = padded.csd
    
new_col = data["class_size"]["CSD"].apply(add_num)
data["class_size"]["padded_csd"] = new_col
    
    
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]

print(data["class_size"].head(10))


## Combining The SAT Scores. Adding all sat individual scores

s1 = data["sat_results"]["SAT Critical Reading Avg. Score"] 
data["sat_results"]["SAT Critical Reading Avg. Score"] = pd.to_numeric(s1, errors="coerce")
s2 = data["sat_results"]["SAT Math Avg. Score"] 
data["sat_results"]["SAT Math Avg. Score"] = pd.to_numeric(s2,errors="coerce")
s3 = data["sat_results"]["SAT Writing Avg. Score"]
data["sat_results"]["SAT Writing Avg. Score"] = pd.to_numeric(s3, errors="coerce")

data["sat_results"]["sat_score"] = data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]

print(data["sat_results"]["sat_score"].head(5))


## Parsing Geographic Coordinates For Schools

import re

def loc(cols):
    s = re.findall("\(.+, .+\)",cols)
    t = s[0].split(",")[0].replace("(", "")
    return t


data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(loc)
print(data["hs_directory"].head(5))


## Extracting The Longitude

import re

def loc(cols):
    s = re.findall("\(.+, .+\)",cols)
    t = s[0].split(",")[1].replace(")", "").strip()
    return t


data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(loc)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

print(data["hs_directory"].head())


##Along the way, we've learned how to:

#Handle files with different formats and columns
#Prepare to merge multiple files
#Use text processing to extract coordinates from a string
#Convert columns from strings to numbers


## END












