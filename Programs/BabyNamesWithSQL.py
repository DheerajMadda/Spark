from pyspark.sql import SparkSession
from pyspark.sql import Row

import collections

# Create a SparkSession (Note, the config section is only for Windows!)
spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("BabySparkSQL").getOrCreate()


def mapper(line):
    fields = line.split(',')
    return Row(Year= int(fields[0]), FirstName=fields[1], County=fields[2], Gender= fields[3],TotalCount=int(fields[4]))


lines = spark.sparkContext.textFile("C:/Spark-codebase/BabyNames.csv")
header = lines.first()

lines = lines.filter(lambda x: x != header)


babies = lines.map(mapper)

schemaBabies = spark.createDataFrame(babies).cache()
schemaBabies.createOrReplaceTempView("Babies")

result = spark.sql("SELECT Year, FirstName, County,Gender, TotalCount FROM Babies WHERE TotalCount >= 165 AND TotalCount <= 300")


result1 = spark.sql("Select FirstName,Count(*),sum(TotalCount) from Babies group by FirstName")

result.show()

result1.show()
