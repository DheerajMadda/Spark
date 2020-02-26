from pyspark import SparkConf, SparkContext
from pyspark.sql import Row

import csv
import string
from io import StringIO

from collections import namedtuple


conf = SparkConf().setMaster('local').setAppName("NewYorkCrimeData")
sc = SparkContext(conf=conf)


mydata = sc.textFile("C:/Spark-codebase/NYPD_7_Major_Felony_Incidents.csv")


header = mydata.first()

mydatawoheader = mydata.filter(lambda x: x != header)

mydatawoheader.map(lambda x: x.split(','))


myfields = header.replace(" ","_").replace("/","_").split(",")

Crime = namedtuple('Crime', myfields, verbose=True)


def parse(row):
    reader = csv.reader(StringIO(row))
    row = next(reader)
    return Crime(*row)


crimes = mydatawoheader.map(parse)

print(crimes.first().Offense)


result = crimes.map(lambda x: x.Offense)

test = result.countByValue()

print(test)


yearsummary = crimes.map(lambda x: x.OccurrenceYear)

test1 = yearsummary.countByValue()

print(test1)

crimesFiltered = crimes.filter(lambda x: not(x.Offense == 'NA' or x.OccurrenceYear == ''))\
    .filter(lambda x: int(x.OccurrenceYear) >= 2006)

test2 = crimesFiltered.map(lambda x:x.OccurrenceYear).countByValue()

print(test2)
