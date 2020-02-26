import re
from pyspark import SparkConf, SparkContext


def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())


conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf=conf)


input = sc.textFile("C:/Spark-codebase/book.txt")
words = input.flatMap(normalizeWords)

output = input.collect()


searchResult = words.filter(lambda x: x == 'risk')


if searchResult.count() == 0:
    print("Not Found")
else:
    print("Found")
    print(searchResult.count())

wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + " " + str(count))
