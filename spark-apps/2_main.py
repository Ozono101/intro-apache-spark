from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

data = [("Spark",), ("Hadoop",), ("Spark",)]
df = spark.createDataFrame(data, ["word"])

df.groupBy("word").count().show()

spark.stop()

# spark-submit --master 'local[4]' 2_main.py
# spark-submit --master 'local[*]' 2_main.py