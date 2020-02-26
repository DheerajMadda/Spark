from pyspark import SparkConf, SparkContext
from pyspark.sql import Row

from datetime import datetime

conf = SparkConf().setMaster('local').setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)


simple_data = sc.parallelize([[1, "Alice", 50], [1, "BOB", 55]])


simple_data.collect()

print(simple_data.count())

print(simple_data.first())





