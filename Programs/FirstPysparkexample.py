from pyspark import SparkConf, SparkContext
from pyspark.sql import Row


conf = SparkConf().setMaster('local').setAppName("FirstProgram")
sc = SparkContext(conf=conf)
simple_data = sc.parallelize([[1,'Alice',50],[2,'Bob',55]])

mylist = simple_data.collect()

print(simple_data.count())
#print(simple_data.first())
for x in mylist:
    print(x)



