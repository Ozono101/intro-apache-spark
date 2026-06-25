from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("demo").getOrCreate()


def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

grade_udf = udf(assign_grade, StringType())

data = [
    ("John", 85),
    ("Mary", 95),
    ("Peter", 72)
]

df = spark.createDataFrame(data, ["name", "score"])

df = df.withColumn("grade", grade_udf(col("score")))

df.show()