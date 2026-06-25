from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.csv("sales.csv", header=True)

clean_df = df.dropna()

clean_df.show()

clean_df.write.mode("overwrite").parquet("output")

spark.stop()

# spark-submit 5_main.py