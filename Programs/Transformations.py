from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("Transformations")
sc = SparkContext(conf=conf)

baby_names = sc.textFile("D:/Scala and Spark Course/SparkCoursePython/BabyNames.csv")

# Map Trasnformation
rows = baby_names.map(lambda line: line.split(","))

for row in rows.take(rows.count()):
    print(row[1])

#    flatMap Trasnformation

print(sc.parallelize([2, 3, 4]).flatMap(lambda x: [x,x,x]).collect())

print(sc.parallelize([1,2,3]).map(lambda x: [x,x,x]).collect())


# filter Transformation
print(rows.filter(lambda line: "JACOB" in line).collect())

# mapPartitions Transformation

one_through_9 = range(1, 10)
parallel = sc.parallelize(one_through_9, 3)

newlst = parallel.collect()


def f(iterator): yield sum(iterator)


print(parallel.mapPartitions(f).collect())

# mapPartitions Another Examples
parallel = sc.parallelize(one_through_9, 8)
newlst1 = parallel.collect()
print(parallel.mapPartitions(f).collect())

print(sc.defaultParallelism)


# union Transformation
one = sc.parallelize(range(1,10))
two = sc.parallelize(range(10,21))
print(one.union(two).collect())
