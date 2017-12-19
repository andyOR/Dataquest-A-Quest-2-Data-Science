## In this script, we will kearn R matrices


## Combine vectors

harvard <- c(1,1,1,1,3)
stanford <- c(2,9,3,4,10)
MIT <- c(3,3,2,2,1)
cambridge <- c(4,2,6,13,48)
oxford <- c(5,7,12,9,15)
columbia <- c(6,13,13,12,4)

uni_vector <- c(harvard,stanford,MIT,cambridge,oxford,columbia)


## creating a matrix

uni_vector <- c(harvard, stanford, MIT, cambridge, oxford, columbia)
uni_matrix <- matrix(data=uni_vector, nrow=6, ncol=5, byrow=True)


## Vector and data types

columbia_types <- c("columbia",6,13,13,12,4)
type <- class(columbia_types)
print(type)


## Naming rows and columns

categories <- c("world_rank","quality_of_education","influence","broad_impact","patents")
universities <- c("Harvard","Stanford","MIT","Cambridge","Oxford","Columbia")

rownames(uni_matrix) <- universities
colnames(uni_matrix) <- categories
named_uni_matrix <- uni_matrix


## Finding the dimension of the matrix

tuition <- c(43280,45000,45016,49350,28450,55161)
print(dim(uni_matrix))
print(length(tuition))
equality <- dim(uni_matrix)[1]==length(tuition)
print(equality)


## Creating new columns and rows

tuition <- c(43280,45000,45016,49350,28450,55161)
uni_matrix <- cbind(uni_matrix, tuition)


## Subsetting And Indexing A Matrix By Element

oxford_influence <- uni_matrix["Oxford","influence"]
stanford_impact <- uni_matrix["Stanford","broad_impact"]
cambridge_patents <- uni_matrix["Oxford","patents"]
MIT_world_rank <- uni_matrix["Oxford","world_rank"]


## Subsetting a matrix by rows and columns

world_rank <- uni_matrix[,"world_rank"]
columbia <- uni_matrix["Columbia",]
patent <- uni_matrix[,"patents"]


## Sorting a matrix

top_edu <- sort(uni_matrix[,"quality_of_education"])
low_cost <- sort(uni_matrix[,'tuition'])


## Using head()

top_edu <- sort(uni_matrix[,"quality_of_education"])
low_cost <- sort(uni_matrix[,"tuition"])
top_two_edu <- head(top_edu,2)
two_low_cost <- head(low_cost,2)


## 




























