## In this script, we will work on a project through command line
## We will working with a dataset of submissions to Hacker News from 2006 to 2015.
## Hacker News is a site where users can submit articles from across the internet
## (usually about technology and startups), and others can "upvote" the articles, signifying that they like them


## Reading The Data

import pandas as pd
def load_data():# function to read data
    f=pd.read_csv("hn_stories.csv")
    f.columns= ["submission_time","upvotes","url","headline"]
    return f


## Which Words Appear In The Headlines Often?

import read
from collections import Counter
df=read.load_data()
count_list=df["headline"]
c=""
for i in count_list:
    c+=str(i)+""
print(Counter(c.lower().split()).most_common(100))


## Which Domains Were Submitted Most Often?

import read
df=read.load_data()
domain_list=df["url"]
values=domain_list.value_counts(sort=True)
print(values[0:100])


## When Are The Most Articles Submitted?

import read
import dateutil as dt
import datetime
df=read.load_data()
def happyhour(h):
    x=dt.parser.parse(h)
    return x.hour

df["hour"]=df["submission_time"].apply(happyhour)
print(df["hour"].value_counts()[0:20])


## END
