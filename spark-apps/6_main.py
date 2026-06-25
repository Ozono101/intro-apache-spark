from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ParquetExample").getOrCreate()

df = spark.read.csv("students.csv",header=True,inferSchema=True)

df.printSchema()
df.show()

df.write.mode("overwrite").parquet("students_parquet")

if __name__ == "__main__":
    spark.stop()