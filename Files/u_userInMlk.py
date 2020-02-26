import collections
from pyspark import SparkConf , SparkContext
from pyspark.sql import  Row


conf= SparkConf().setMaster('local').setAppName("ProgSales")
sc=SparkContext(conf=conf)
rdd=sc.textFile("D:/spark Code Base/Spark-codebase/ml-100k/u.user")

newRdd=rdd.map(lambda line:line.split('|'))

myrdd1=newRdd.map(lambda x:(x[2],1)).reduceByKey(lambda v,y:v+y).sortBy(lambda a:a[1],ascending=False).collect() #number by gender
myrdd2=newRdd.map(lambda x:(x[3],1)).reduceByKey(lambda v,y:v+y).collect() #number by coccupation
print(myrdd2[0])
myrdd3=newRdd.map(lambda x:(x[2],x[3])).map(lambda v:(v,1)).reduceByKey(lambda s,y:s+y).collect() #work on this no. by gender and occupation
print(myrdd3[0])
#myrdd4=myrdd3.map(lambda x:(x,1)).reduceByKey(lambda v,y:v[1]+y[1]).collect()
#lstRdd=list(myrdd4)
#print(lstRdd)
#print(myrdd4[0])
for s in myrdd1:
    print(s[0],":",s[1])

for s in myrdd2:
    print(s[0],":",s[1])

for s in myrdd3:
    print(s[0][1],":",s[0][0],":",s[1])
