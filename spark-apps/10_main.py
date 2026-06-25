from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv(
    "students.csv",
    header=True,
    inferSchema=True
)

print(f"Total records: {df.count()}")
df.show()

departments = ["Physics", "Mathematics", "Biology"]

for dept in departments:
    df.filter(df.department == dept) \
      .coalesce(1) \
      .write \
      .mode("overwrite") \
      .option("header", True) \
      .csv(f"reports/{dept}")

spark.stop()

# spark-submit  --master local[*] --num-executors 2 --executor-cores 2 --executor-memory 1G --driver-memory 1G 10_main.py