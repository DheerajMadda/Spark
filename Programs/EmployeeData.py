from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("EmployeeDataDF").getOrCreate()

lines = spark.read.json("C:/Spark-codebase/Employee.json")
lines.printSchema()
lines.show()
lines.createOrReplaceTempView("EmpJsonData")
lines.select("name").show()
lines.filter(lines["age"] >23).show()

lines.groupBy("age").count().show()

spark.sql("select count(age),name from EmpJsonData group by age, name").show()