from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg


spark = SparkSession.builder.appName("demo").getOrCreate()

df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13),
    ],
    ["first_name", "age"],
)

df.show()


# Add a new column "life_stage" based on the age
df1 = df.withColumn(
    "life_stage",
    when(col("age") < 13, "child")
    .when(col("age").between(13, 19), "teenager")
    .otherwise("adult"),
)

df1.show()

# now show only teenagers and adults
df1.where(col("life_stage").isin(["teenager", "adult"])).show()


# Calculate the average age of the teenagers and adults
df1.select(avg("age")).show()

# Group by life stage and calculate the average age
df1.groupBy("life_stage").avg().show()

# Register the DataFrame as a temporary view
df1.createOrReplaceTempView("people")

# Use the temporary view to run a SQL query
spark.sql("select avg(age) from people").show()

# Group by life stage and calculate the average age using SQL
spark.sql("select life_stage, avg(age) from people group by life_stage").show()

# Save the DataFrame as a table
df1.write.saveAsTable("some_people")

# Query the saved table
spark.sql("select * from some_people").show()

# Insert a new row into the saved table
spark.sql("INSERT INTO some_people VALUES ('frank', 4, 'child')")

spark.sql("select * from some_people").show()

# Query the saved table for a specific life stage
spark.sql("select * from some_people where life_stage='teenager'").show()