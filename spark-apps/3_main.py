import sys
from pyspark.sql import SparkSession

input_file = sys.argv[1]

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

df = spark.read.csv(input_file, header=True)

df.show()

spark.stop()

# spark-submit --master 'local[*]' --executor-memory 1G --driver-memory 1G 3_main.py sales.csv