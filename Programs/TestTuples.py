from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("StudentScores")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([['Amit',48],['Mohan',45], ['Suhas', 50]])

newrdd = rdd.collectAsMap()

k = list(newrdd.keys())
v = list(newrdd.values())
print(k[v.index(max(v))])


for keys,values in newrdd.items():
    print(keys)
    print(values)