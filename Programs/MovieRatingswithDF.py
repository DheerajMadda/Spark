from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

import collections

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("DFfromCSV").getOrCreate()

lines = spark.sparkContext.textFile("C:/Spark-codebase/ml-100k/u.data")

movies = lines.map(lambda x: Row(movieRating=int(x.split()[2])))

movieDataframe = spark.createDataFrame(movies)

test = movieDataframe.select("movieRating").groupBy("movieRating").count()

test.show()
