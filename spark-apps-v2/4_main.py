from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("S3ETL").getOrCreate()

df = spark.read.csv("s3a://ai-ml-course/students.csv", header=True, inferSchema=True)

df.write.mode("overwrite").parquet("s3a://ai-ml-course/output/")

if __name__ == "__main__":
    spark.stop()