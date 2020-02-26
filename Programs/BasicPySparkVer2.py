from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext


spark = SparkSession.builder.master("local").config(conf=SparkConf()).getOrCreate()

mysqlcontext = SQLContext(spark)

print(mysqlcontext)

simple_data = [[1, "Alice", 50], [1, "BOB", 55]]

rdd = spark.sparkContext.parallelize(simple_data)

b = spark.createDataFrame(rdd, ['Id', 'Name', 'Age'])

a = spark.createDataFrame([[1, "a"], [2, "b"], [3, "c"], [4, "d"], [5, "e"]], ['ind', "state"])
a.show()
a.printSchema()

b.show()

df = mysqlcontext.range(5)
df.show()

mysqlcontext.createDataFrame(simple_data, ['Id', 'Name', 'Age']).show()
