from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("CustomerSpendwithDF").getOrCreate()

lines = spark.sparkContext.textFile("C:/Spark-codebase/customer-orders.csv")
customers = lines.map(lambda x: x.split(","))
customersDF = spark.createDataFrame(customers)

customersDF = customersDF.withColumnRenamed("_1", "CustID")
customersDF = customersDF.withColumnRenamed("_2", "OrderID")
customersDF = customersDF.withColumnRenamed("_3", "Sales")

#customersDF.show()


customerSpent = customersDF.groupBy("CustID").agg({"Sales":"sum"}).orderBy("sum(Sales)",ascending=False).show(1)

