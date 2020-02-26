from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("SumRDD")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(['Hello There and How are you', 'World'])

newrdd = sc.parallelize([1, 10, 15, 30, 35, 30, 15, 10])

mylst = newrdd.filter(lambda x: x > 10)

mylst.foreach(print)

print(mylst)

lst = rdd.collect()

newlst = reversed(lst)

for x in newlst:
     print(x[::-1])


rddflatmap = rdd.flatMap(lambda x: x.split(' '))

rddflatmap.foreach(print)


rddduniquevalues = newrdd.distinct()

rddduniquevalues.foreach(print)
