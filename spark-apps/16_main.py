from pyspark.sql.functions import pandas_udf
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql.types import DoubleType


spark = SparkSession.builder.appName("demo").getOrCreate()


data = [
    ("John", "Doe"),
    ("Mary", "Smith")
]

df = spark.createDataFrame(data, ["first_name", "last_name"])

@pandas_udf("string")
def upper_pandas(col: pd.Series) -> pd.Series:
    return col.str.upper()

# Example usage:
df.withColumn("upper_name", upper_pandas("first_name")).show()  