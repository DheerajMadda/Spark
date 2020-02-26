from pyspark import SparkConf, SparkContext
import collections
from collections import Counter

from pyspark.sql import Row

conf = SparkConf().setMaster('local').setAppName("GenderCount")
sc = SparkContext(conf=conf)

lines = sc.textFile("C:/Spark-codebase/ml-100k/u.user")

newrdd = lines.map(lambda line: line.split("|"))

newrdd1 = newrdd.map(lambda m:(m[2], 1)).reduceByKey(lambda x,y: x + y).collect()


occupationData = newrdd.map(lambda n: (n[3], 1)).reduceByKey(lambda y, z: y + z).collect()

testrdd = newrdd.map(lambda x:(x[3],(x[2],1))).map(lambda a:((a[0],a[1][0]),a[1][1])).reduceByKey(lambda a,b:a+b).collect()


for elem in sorted(testrdd):
    print(elem[0][0],elem[0][1],elem[1])
    # print(elem[0][0])
    # if elem[0][1] == 'M':
    #    print("The number of Males are :", elem[1])
    # else:
    #     print("The number of FeMales are :", elem[1])

# for e in occupationData:
#     print(e)
