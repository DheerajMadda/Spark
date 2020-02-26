from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("SumRDD")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([5, 20, 45, 95, 200, 30, 500])

print(rdd.sum())

print(rdd.count())

newrdd = rdd.map(lambda x: x * x)

newrdd.foreach(print)

newrdd1 = rdd.filter(lambda x: x > 50)

print("RDD with values > 50")
newrdd1.foreach(print)


print("Mean is", newrdd.mean())




