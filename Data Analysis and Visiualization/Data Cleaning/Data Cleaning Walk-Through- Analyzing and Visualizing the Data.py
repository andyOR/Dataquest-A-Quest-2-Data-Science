## In this scripts, we will discover correlations, create plots, and then make maps
## using New York city Public Schools dataset


## Finding Correlations With The R Value. "r" value is called Pearson's correlation coefficient
#  pandas.DataFrame.corr() method is used to find correlations between columns in a dataframe


## Finding Correlations With The R Value

correlations = combined.corr()
correlations = correlations["sat_score"]
print(correlations)


## Plotting Enrollment With The Plot() Accessor. We can plot columns in a dataframe using the pandas.DataFrame.plot() accessor on a dataframe

import matplotlib.pyplot as plt

combined.plot.scatter(x = "total_enrollment", y= "sat_score")


## Exploring Schools With Low SAT Scores And Enrollment

low_enrollment = combined[combined["total_enrollment"] < 1000]
low_enrollment = low_enrollment[low_enrollment["sat_score"] < 1000]
print(low_enrollment["School Name"])


## Plotting Language Learning Percentage. This number of english language learner percent

combined.plot.scatter(x = "ell_percent", y = "sat_score")


## Mapping The Schools With Basemap

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

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()


m.scatter(longitudes, latitudes, s =20, zorder=2, latlon=True)

plt.show()


## Plotting Out Statistics. Using colors for range of values

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

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()


m.scatter(longitudes, latitudes, s =20, zorder=2, latlon=True, c = combined["ell_percent"], cmap="summer")

plt.show()


##Calculating District-Level Statistics

import numpy

districts = combined.groupby("school_dist").agg(numpy.mean) ## grouping on school_dist values and finding mean value
print(districts)
districts.reset_index(inplace = True)

print(districts.head())

## Plotting Percent Of English Learners By District. Using districts now to plot percent of english learners

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


m.scatter(longitudes, latitudes, s =50, zorder=2, latlon=True, c = districts["ell_percent"], cmap="summer")

plt.show()


##Along the way, we learned:

#How to create school and district-level maps
#How to find correlations, and what those correlations mean
#Why we should plot data out, rather than relying on the r value alone
#That ell_percent has a strong negative correlation with sat_score


## END
