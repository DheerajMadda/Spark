from pyspark import SparkConf, SparkContext
from pyspark.sql import Row
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.evaluation import MulticlassMetrics

conf = SparkConf().setMaster('local').setAppName("Wine Prediction")
sc = SparkContext(conf=conf)


rawdata = sc.textFile("C:/Spark-codebase/wine.data")
print(rawdata.take(5))

def parsePoint(line):
    values = [float(x) for x in line.split(',')]
    return LabeledPoint(values[0],values[1:])

parsedData = rawdata.map(parsePoint)
print(parsedData.take(5))

(trainingData,testData) = parsedData.randomSplit([0.7,0.3])

model = DecisionTree.trainClassifier(trainingData,numClasses=4,categoricalFeaturesInfo={},impurity='gini',maxDepth=3,maxBins=32)

predictions = model.predict(testData.map(lambda x:x.features))
print(predictions.take(5))

labelsAndPredictions = testData.map(lambda lp:lp.label).zip(predictions)
print(labelsAndPredictions.take(5))

testAccuracy = labelsAndPredictions.filter(lambda lp: lp[0] == lp[1]).count()/float(testData.count())
print('Test Accuracy: ',testAccuracy)

metrics = MulticlassMetrics(labelsAndPredictions)
print('Metrics.accuracy: ',metrics.accuracy)
print('Metrics.fmeasure: ',metrics.fMeasure())
print('Precision for 1.0:',metrics.precision(1.0))
print('Precision for 3.0:',metrics.precision(3.0))

print('Confusion Metrics:',metrics.confusionMatrix().toArray())

print(model.toDebugString())