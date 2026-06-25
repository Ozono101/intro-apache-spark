import sys
from pyspark.sql import SparkSession

input_file = sys.argv[1]
output_file = sys.argv[2]

spark = SparkSession.builder.appName("ProcessData").getOrCreate()

df = spark.read.csv(input_file, header=True, inferSchema=True)

df.write.mode("overwrite").parquet(output_file)

spark.stop()

# https://spark.apache.org/docs/latest/submitting-applications.html

# spark-submit 11_main.py students.csv output/
# spark-submit --master local[*] --driver-memory 1G --executor-memory 1G --executor-cores 2 11_main.py students.csv output/
# spark-submit --conf spark.sql.shuffle.partitions=8 --conf spark.executor.memory=4g --conf spark.driver.memory=2g 11_main.py