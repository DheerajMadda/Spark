from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName('Testy')
sc = SparkContext(conf=conf)


# baby_names = sc.textFile("D:/Scala and Spark Course/SparkCoursePython/BabyNames.csv")
#
# # Map Trasnformation
# rows = baby_names.map(lambda line: line.split(","))
#
# for row in rows.take(rows.count()):
#     print(row[1], row[3])
#
#
# print("with flatmap")
# print(sc.parallelize([2, 3, 4]).flatMap(lambda x: [x,x,x]).collect())
#
#
# print("with map")
# print(sc.parallelize([1,2,3]).map(lambda x: [x,x,x]).collect())
#
#
# rdd = sc.parallelize(["Hello World High", "This World is great", "How are you", "This and That and That" ])
#
# newrdd = rdd.collect()
#
# scount = 0
#
# for x in newrdd:
#     if "World" in x:
#         scount += 1
#         print(x.replace("World", "Word"))
#         print(x)
# if scount > 0:
#     print("Found ", scount, "times")
#
#
