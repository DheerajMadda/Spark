from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import Row

import collections

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("NSparkSQL").getOrCreate()

newrdd = spark.sparkContext.parallelize([[1, "Alice", 50], [1, "BOB", 55]])

df = newrdd.toDF()

df.show()



