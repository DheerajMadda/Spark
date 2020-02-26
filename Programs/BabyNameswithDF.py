from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
import pyspark.sql.functions as func

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("BabyNames").getOrCreate()

lines = spark.sparkContext.textFile("C:/Spark-codebase/BabyNames.csv")

header = lines.first()

lines = lines.filter(lambda x: x != header)


babynames = lines.map(lambda x: x.split(","))

totalcount = babynames.count()


babynamesDF = spark.createDataFrame(babynames, schema=header.split(","))

babynamecountDF = babynamesDF.select("FirstName").groupBy("FirstName").count()

babynamessumDF = babynamesDF.agg({"Count": "sum"})
babynamessumDF = babynamessumDF.withColumnRenamed("sum(count)","AggrCount")

babynamecountDF.show()

babynamessumDF.show()

result = babynamessumDF.collect()
total = 0
for n in result:
    total = n[0]
print(total)


babynameswithcount = babynamesDF.select("FirstName","Count").groupBy("FirstName").agg({"Count": "sum"})

babynameswithcount = babynameswithcount.withColumnRenamed("sum(Count)","IndCount")
babynameswithcount.show()

babynamespc = babynameswithcount.withColumn("Percent Contribution", func.round((babynameswithcount.IndCount/total)*100, 2))

babynamespc.orderBy(babynamespc[2].desc()).show()


babynamesDF = babynamesDF.select("Sex").groupBy("Sex").count()

babynamesDF.show()

data = babynamesDF.collect()

test = list()

for m in data:
    if m[0] == 'F':
        print("No.of Females: ", m[1])
        print("% of Females: ", format(((m[1]*100)/totalcount), '.2f'))
        test.append(m[1])
    else:
        print("No. of Males:", m[1])
        print("% of Males: ", format(((m[1]*100)/totalcount), '.2f'))
        test.append(m[1])

print(max(test))
