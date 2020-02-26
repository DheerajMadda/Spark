from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

import collections

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("DFfromCSV").getOrCreate()


rdd = spark.sparkContext.parallelize([['Tom'], ['Jack'], ['Tom'], ['Isabella'], ['Tom'], ['Jerry'], ['Donald'], ['Jerry']])

strDataFrame = spark.createDataFrame(rdd)

strDataFrame = strDataFrame.withColumnRenamed("_1", "Name")

test = strDataFrame.select("Name").groupBy("Name").count()

test.show()