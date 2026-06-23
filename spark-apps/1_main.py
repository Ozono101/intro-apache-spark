from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DockerTest").getOrCreate()

df = spark.createDataFrame([("Alice", 25), ("Bob", 30)], ["Name", "Age"])

if __name__ == "__main__":
    df.show()
    spark.stop()
