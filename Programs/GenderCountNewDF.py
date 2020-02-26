from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("BabyNames").getOrCreate()

lines = spark.sparkContext.textFile("C:/Spark-codebase/ml-100k/u.user")

users = lines.map(lambda x: x.split("|"))
usersDF = spark.createDataFrame(users)
cols = list(["Id","Age","Gender","Profession","refID"])
print(cols)
usersDF = usersDF.withColumnRenamed("_1", "Id")
usersDF = usersDF.withColumnRenamed("_2", "Age")
usersDF = usersDF.withColumnRenamed("_3", "Gender")
usersDF = usersDF.withColumnRenamed("_4", "Profession")
usersDF = usersDF.withColumnRenamed("_5", "refId")

usersDF.printSchema()
#usersDF.show()
usersDF.createOrReplaceTempView("OccupationData")

countrec = spark.sql("Select Profession,Gender,count(Gender) from OccupationData group by Profession,Gender").show()


test = usersDF.select("Profession","Gender").groupBy("Profession","Gender").count()
#test.show()