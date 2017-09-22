## While the Spark toolkit is in Scala, a language that compiles down to bytecode for the JVM,
## the open source community has developed a wonderful toolkit called PySpark that allows us
## to interface with RDDs in Python.

## Resilient Distributed Data Sets (RDDs)

raw_data = sc.textFile("daily_show.tsv")
raw_data.take(5)


## SparkContext
# In Spark, the SparkContext object manages the connection to the clusters, and coordinates the running of processes on those clusters.


## Lazy Evaluation


## Pipelines

daily_show = raw_data.map(lambda line: line.split('\t'))
print(daily_show.take(5))


## ReduceByKey()

tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)
print(tally)


##  Explanation

tally.take(tally.count())


## Filter

def filter_year(line):
    # Write your logic here
    if line[0]!= 'YEAR':
        return True


## Practice with Pipelines

filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)


END
