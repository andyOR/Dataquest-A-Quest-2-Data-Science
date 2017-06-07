## In this script, we will learn to visualize data on maps using geographic datasets
## Dataset from openflights.org for airlines, airports and routes



## Geographic datasets

import pandas as pd

airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
routes = pd.read_csv("routes.csv")

print(airlines.iloc[0])
print(airports.iloc[0])
print(routes.iloc[0])


## Geographic Coordinate Systems


## Installing Basemap


## Workflow With Basemap. we will use basemap_constructor() with parameters
#projection: the map projection.
#llcrnrlat: latitude of lower left hand corner of the desired map domain
#urcrnrlat: latitude of upper right hand corner of the desired map domain
#llcrnrlon: longitude of lower left hand corner of the desired map domain
#urcrnrlon: longitude of upper right hand corner of the desired map domain

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection= "merc", llcrnrlat= -80, urcrnrlat= 80, llcrnrlon= -180, urcrnrlon= 180)


## Converting From Spherical To Cartesian Coordinates

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()

x,y = m(longitudes, latitudes)
print(longitudes[0:5])
print(latitudes[0:5])
print(x[0:5])
print(x[0:5])


## Generating A Scatter Plot

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)
m.scatter(x,y, s =1) # scatter plot with marker size of 1
plt.show()


## Customizing The Plot Using Basemap. Drawing coastlines of continents

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()


## Customizing The Plot Using Matplotlib. modifying size of the plot using pyplot() and adding title to scatter plot

# Add code here, before creating the Basemap instance.
fig, ax = plt.subplots(figsize=(15,20))
ax.set_title("Scaled Up Earth With Coastlines")

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()


## Introduction To Great Circles. This will be used to create paths between aiports on maps

geo_routes = pd.read_csv("geo_routes.csv")
geo_routes.info()
geo_routes[0:5]


## Displaying Great Circles. Displaying all connection from DFW aiport using drawgreatcirlces()

for index, row in df.iterrows():
        end_lat, start_lat = row['end_lat'], row['start_lat']
        end_lon, start_lon = row['end_lon'], row['start_lon']
        
        if abs(end_lat - start_lat) < 180:
            if abs(end_lon - start_lon) < 180:
                m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)

soc = geo_routes["source"] == "DFW"
dfw = geo_routes[soc]
create_great_circles(dfw)
plt.show()

## END












