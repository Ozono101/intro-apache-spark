from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("demo").getOrCreate()

def get_domain(email):
    return email.split("@")[1]

domain_udf = udf(get_domain, StringType())

data = [
    ("john@gmail.com",),
    ("mary@yahoo.com",),
    ("peter@outlook.com",)
]

df = spark.createDataFrame(data, ["email"])

df = df.withColumn("domain", domain_udf(col("email")))

df.show()