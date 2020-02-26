from pyspark import SparkConf, SparkContext

import collections
from collections import Counter


conf = SparkConf().setMaster('local').setAppName("Superstore")
sc = SparkContext(conf=conf)

rdd = sc.textFile("C:/Spark-codebase/SampleSuperstore.csv")

newrdd = rdd.map(lambda line: line.split(","))

header = newrdd.first()

myrdd = newrdd.filter(lambda m: m != header)

myrdd1 = myrdd.map(lambda s: (s[7], float(s[2]))).reduceByKey(lambda v, y: v + y).\
    sortBy(lambda a: a[1],ascending=False).collect()

for x in myrdd1:
    print(x[0],":",format(x[1], '.2f'))


