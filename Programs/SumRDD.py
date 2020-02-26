from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("SumRDD")
sc = SparkContext(conf=conf)
lines = sc.parallelize([1,5,10,15,30])

print(lines.sum())
