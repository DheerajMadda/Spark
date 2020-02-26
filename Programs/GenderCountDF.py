from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("GenderCountDF").getOrCreate()

lines = spark.sparkContext.textFile("D:/Scala and Spark Course/SparkCoursePython/StudentScores.csv")

header = lines.first()

lines = lines.filter(lambda x: x != header)


students = lines.map(lambda x: x.split(","))

studentsDF = spark.createDataFrame(students, schema=header.split(","))
studentsDF.show()
studentsCount = studentsDF.select("studentname","Total").count()


print("Total Number of Students :",studentsCount)


highestScore = studentsDF.select("studentname","Total").agg({"Total": "max"}).collect()[0][0]

print("Highest Score is:",highestScore)

