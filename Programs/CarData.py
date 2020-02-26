from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("EmployeeDataDF").getOrCreate()

lines = spark.read.json("C:/Spark-codebase/cars.json")
lines.printSchema()
lines.show()

lines.select("name").show()
lines.filter(lines["speed"] >250).show()

lines.groupBy("name","weight").agg({"weight":"max"}).orderBy("weight",ascending=False).show(1)

