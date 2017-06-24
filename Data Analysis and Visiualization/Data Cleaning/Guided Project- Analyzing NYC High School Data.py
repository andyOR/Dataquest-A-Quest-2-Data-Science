## In this cahllenge, we will dive deep into NYC school data and assess relation among variables with significant correlations


## Introduction

import matplotlib.pyplot as plt
%matplotlib inline
combined.corr()["sat_score"][survey_fields].plot.bar()


## Exploring Safety And SAT Scores

plt.scatter( combined["saf_s_11"], combined["sat_score"])

#From the scatter plot of "saf_s_11" and "sat_score", it seems a positive correlation between this two variables but not strong relation.
#There is cluster at the bottom and few schools with high sat_score and safety score.

import numpy

districts = combined.groupby("school_dist").agg(numpy.mean)

from mpl_toolkits.basemap import Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = districts["lon"].tolist()
latitudes = districts["lat"].tolist()


m.scatter(longitudes, latitudes, s =50, zorder=2, latlon=True, c = districts["saf_s_11"], cmap="summer")

plt.show()


## Exploring Race And SAT Scores

race_fields = ["white_per","asian_per","black_per","hispanic_per"]
combined.corr()["sat_score"][race_fields].plot.bar()


print(combined[combined["hispanic_per"]> 95]["SCHOOL NAME"])

print(combined[(combined["hispanic_per"]< 10) & (combined["sat_score"]>1800)]["SCHOOL NAME"])


## Exploring Gender And SAT Scores

gender_fields = ["male_per","female_per"]
combined.corr()["sat_score"][gender_fields].plot.bar()

combined.plot.scatter("female_per", "sat_score")

print(combined[(combined["female_per"]> 60) & (combined["sat_score"]>1700)]["SCHOOL NAME"])


## Exploring AP Scores Vs. SAT Scores

combined["ap_per"] = combined["AP Test Takers "]/combined["total_enrollment"]

plt.scatter(combined["ap_per"], combined["sat_score"])


## END
























