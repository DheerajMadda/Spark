from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("ConvertToUpper")
sc = SparkContext(conf=conf)
lines = sc.textFile("C:/Spark-codebase/ml-100k/README")


linesInUpper = lines.map(lambda x: x.upper())

result = linesInUpper.collect()

for x in result:
    print(x)
