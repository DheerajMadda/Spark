from pyspark import SparkConf, SparkContext
import collections
from collections import Counter

conf = SparkConf().setMaster('local').setAppName("StudentScores")
sc = SparkContext(conf=conf)

rdd = sc.textFile("D:/Scala and Spark Course/SparkCoursePython/StudentScores.csv")

newrdd = rdd.map(lambda line: line.split(","))

header = newrdd.first()


myrdd = newrdd.filter(lambda m: m != header)
studentdatawoheader = newrdd.filter(lambda m: m != header).collect()

#variables for converting to dictionary

totalmarks = 0
marksforcalc = list()
marksfordict = list()
temp = list()

for o in studentdatawoheader:
      temp = ([o[1], int(o[4])])
      marksfordict.append(temp)

temprdd = sc.parallelize(marksfordict)


trdd = temprdd.collectAsMap()

#highest score and scorer

k = list(trdd.keys())
v = list(trdd.values())
print("Highest Scorer is: ", k[v.index(max(v))])

#Top 3 Scores
comm = Counter(trdd)
high = comm.most_common(3)

print("\nTop 3 Scorers:")
for y in high:
    print(y)

# Avg of Total Marks

for z in studentdatawoheader:
    totalmarks += int(z[4])
    marksforcalc.append(int(z[4]))

print("\n")
print("Avg of Total Marks: ", format(totalmarks/len(studentdatawoheader), '.2f'))

# Max of Total Marks
print("\n")
print("Highest Score : ", max(marksforcalc))
print("Lowest Score  : ", min(marksforcalc))
