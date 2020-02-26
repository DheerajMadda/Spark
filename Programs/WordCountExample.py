from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("WordCount")
sc = SparkContext(conf=conf)
lines = sc.textFile("C:/Spark-codebase/ml-100k/README")

wordCount = lines.map(lambda x: x.split())


res = wordCount.count()
print(res)
