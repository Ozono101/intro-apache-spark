from pyspark.sql import SparkSession


# spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.appName("ReadS3CSV").getOrCreate()


df = spark.read.option("header", "true").option("inferSchema", "true").csv("s3a://ai-student-bucket-2026/sales.csv")

df.show()

# spark-submit --packages org.apache.hadoop:hadoop-aws:3.4.1 --master 'local[*]' --executor-memory 1G --driver-memory 1G 4_main.py
# spark-submit --master 'local[*]' --executor-memory 1G --driver-memory 1G 4_main.py