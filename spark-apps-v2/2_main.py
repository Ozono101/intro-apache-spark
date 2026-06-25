from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("ParquetExample").getOrCreate()

    df = spark.read.csv("students.csv",header=True,inferSchema=True)

    df.printSchema()

    df.show(2)

    df.write.mode("overwrite").parquet("students_parquet")

    spark.stop()

if __name__ == "__main__":
    main()
    