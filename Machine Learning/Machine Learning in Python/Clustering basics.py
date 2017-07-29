## Clustering is a key way to explore unknown data, and it's a very commonly used machine learning technique.
## In this script, we'll work on clustering US Senators based on how they voted


## The Dataset

import pandas as pd
votes = pd.read_csv("114_congress.csv")
print(votes.head())


## Exploring The Data

print(votes['party'].value_counts())
print(votes.mean())


## Distance Between Senators

from sklearn.metrics.pairwise import euclidean_distances

print(euclidean_distances(votes.iloc[0,3:].reshape(1, -1), votes.iloc[1,3:].reshape(1, -1)))
distance = euclidean_distances(votes.iloc[0,3:].reshape(1, -1), votes.iloc[2,3:].reshape(1, -1))


## Initial Clustering

import pandas as pd
from sklearn.cluster import KMeans

kmeans_model = KMeans(n_clusters=2, random_state=1)
columns = votes.columns[3:]
senator_distances = kmeans_model.fit_transform(votes[columns])


## Exploring The Clusters

labels = kmeans_model.labels_
pd.crosstab(labels, votes["party"])


## Exploring Senators In The Wrong Cluster

democratic_outliers = votes[(labels==1) & (votes["party"]=="D")]
print(democratic_outliers)


## Plotting Out The Clusters

plt.scatter(senator_distances[:,0], senator_distances[:,1], c =labels)
plt.xlabel("Cluster 1")
plt.ylabel("Cluster 2")
plt.title("Clustering Democrats Vs. Republican")
plt.show()


## Finding The Most Extreme

extremism = (senator_distances ** 3).sum(axis=1)
votes["extremism"] = extremism
votes.sort_values("extremism", inplace=True, ascending = False)
print(votes.head(10))


## 
