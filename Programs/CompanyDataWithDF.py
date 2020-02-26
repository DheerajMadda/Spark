from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("CompanyData").getOrCreate()

emplines = spark.sparkContext.textFile("C:/Spark-codebase/CompanyEMP.csv")


empheader = emplines.first()

elines = emplines.filter(lambda x: x != empheader)

employees = elines.map(lambda x: x.split(","))

employeesDF = spark.createDataFrame(employees, schema=empheader.split(","))


deptlines = spark.sparkContext.textFile("C:/Spark-codebase/CompanyDEPT.csv")

deptheader = deptlines.first()

dlines = deptlines.filter(lambda x: x != deptheader)

departments = dlines.map(lambda x: x.split(","))

departmentsDF = spark.createDataFrame(departments, schema=deptheader.split(","))


joinedtable = employeesDF.join(departmentsDF, employeesDF.DeptId == departmentsDF.DeptId)

joinedtable.createOrReplaceTempView("Company")

genderdf = spark.sql("SELECT  DepartmentName, Gender,count(*) as GenderCount from Company group by DepartmentName,Gender")

genderdf.show()

deptselect = spark.sql("SELECT * from Company where DepartmentName in ('IT','HR')")
deptselect.show()
