from pyspark import SparkConf, SparkContext
import collections
from collections import Counter

conf = SparkConf().setMaster('local').setAppName("Reversed")
sc = SparkContext(conf=conf)

lines = sc.textFile("C:/Spark-codebase/ml-100k/README")

splitlines = lines.map(lambda line: line.split("\n")).collect()
splitwords = lines.map(lambda line: line.split(" ")).collect()


splitlines.reverse()
countword = 0
searchstr = "data"
replacestr = "DATA"

for x in splitlines:
    x = [w.replace(searchstr,replacestr)for w in x]
    print(x)


for t in splitwords:
    if searchstr in t:
        countword += 1

print("The word ", searchstr, "found ", countword, " times")

