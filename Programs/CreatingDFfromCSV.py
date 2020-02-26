from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

import collections

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("DFfromCSV").getOrCreate()

df = spark.read.csv("D:/Scala and Spark Course/SparkCoursePython/StudentScores.csv", mode= "DROPMALFORMED", inferSchema= True, header = True)

df.printSchema()

df.select('studentname', 'Total').show()

# print(df.filter(df.Total >= 45).count())

df.select('studentname', 'Total').filter(df.Total <= 43).show()

df.select('studentname', df.Total * 2).show()

scount = df.select('Total').count()



test = df.collect()

total = 0
for m in test:
    total += m[4]
print(format((total/scount), '0.2f'))