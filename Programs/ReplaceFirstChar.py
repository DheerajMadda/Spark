from pyspark import SparkConf, SparkContext
from pyspark.sql import Row

from datetime import datetime

conf = SparkConf().setMaster('local').setAppName("ReplaceFirstChar")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(['Jack', 'Tom', 'Donald'])


newrdd = rdd.collect()

newrdd.sort()


for x in newrdd:
    print(x.lower())


