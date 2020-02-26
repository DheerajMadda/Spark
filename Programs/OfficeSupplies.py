from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName("OfficeSupplies")
sc = SparkContext(conf=conf)

rdd = sc.textFile("D:/Scala and Spark Course/SparkCoursePython/OfficeSupplies.csv")

newrdd = rdd.map(lambda line: line.split(","))

header = newrdd.first()

myrdd = newrdd.filter(lambda m: m != header)



#officedatawoheader = newrdd.filter(lambda m: m != header).collect()


myrdd1 = myrdd.map(lambda s: (s[2], float(s[6]))).reduceByKey(lambda v, y: v + y).\
    sortBy(lambda a: a[1],ascending=False).collect()


#myrdd1.sort()


print("Sales Rep wise Sales:")
for elem in myrdd1:
    print(elem[0], ":", format(elem[1], '.2f'))

print("Sales Rep with highest Sales: ", myrdd1[0])