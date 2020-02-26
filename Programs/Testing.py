from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("TestDataDF").getOrCreate()

lines = spark.sparkContext.textFile("C:/Spark-codebase/TestData.csv")
testdata = lines.map(lambda x: x.split(","))
testDF = spark.createDataFrame(testdata)

testDF = testDF.withColumnRenamed("_1", "Company")
testDF = testDF.withColumnRenamed("_2", "Person")
testDF = testDF.withColumnRenamed("_3", "Sales")

newdata = testDF.groupBy('Company').agg({"Sales":"sum"}).orderBy("sum(Sales)",ascending=False).show(1)



