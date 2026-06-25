from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql.types import DoubleType


spark = SparkSession.builder.appName("demo").getOrCreate()

sales_data = [
    ("Laptop", 1000),
    ("Phone", 800),
    ("Tablet", 500)
]

age_data = [
    ("John", 85),
    ("Mary", 95),
    ("Peter", 72)
]


sales_df = spark.createDataFrame(sales_data, ["product", "price"])
age_df = spark.createDataFrame(age_data, ["name", "age"])

sales_df.show()
age_df.show()


def add_tax(price):
    return price * 1.10

def age_group(age):
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

tax_udf = udf(add_tax, DoubleType())
age_group_udf = udf(age_group, StringType())

sales_df.withColumn("price_with_tax",tax_udf("price")).show()
age_df.withColumn("age_group",age_group_udf("age")).show()