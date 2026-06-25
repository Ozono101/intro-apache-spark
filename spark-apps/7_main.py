from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Departments").getOrCreate()

data = [
    (1, "John", "Computer Science", 85),
    (2, "Mary", "Computer Science", 92),
    (3, "Peter", "Mathematics", 78),
    (4, "Sarah", "Mathematics", 88),
    (5, "David", "Physics", 91),
    (6, "Alice", "Physics", 83),
    (7, "Michael", "Biology", 79),
    (8, "Emma", "Biology", 95)
]

columns = ["student_id", "name", "department", "score"]

df = spark.createDataFrame(data, columns)
df.show()

cs_df = df.filter(df.department == "Computer Science")
cs_df.show()

math_df = df.filter(df.department == "Mathematics")
math_df.show()

phys_df = df.filter(df.department == "Physics")
phys_df.show()

bio_df = df.filter(df.department == "Biology")
bio_df.show()

cs_df.write.mode("overwrite").option("header", True).csv("departments/computer_science")

math_df.write.mode("overwrite").option("header", True).csv("departments/mathematics")

phys_df.write.mode("overwrite").option("header", True).csv("departments/physics")

bio_df.write.mode("overwrite").option("header", True).csv("departments/biology")

df.write.mode("overwrite").partitionBy("department").parquet("departments_parquet")

if __name__ == "__main__":
    spark.stop()