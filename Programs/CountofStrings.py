from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("StringCount")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(['Tom', 'Jack', 'Tom', 'Isabella', 'Tom', 'Jerry', 'Donald', 'Jerry'])

maprdd = rdd.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

maprdd.foreach(print)

mylst = rdd.collect()

mylst1 = reversed(mylst)
for x in mylst1:
    print(x)
    print(x[::-1])
