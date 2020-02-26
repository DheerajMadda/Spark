from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("LineCount")
sc = SparkContext(conf=conf)
lines = sc.textFile("C:/Spark-codebase/ml-100k/README")

print(lines.count())
