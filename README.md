## What is Apache Spark?
Apache Spark is a fast, distributed data processing framework used for:

- Big Data Analytics
- Data Engineering
- Machine Learning
- Streaming Data Processing
- ETL Pipelines
- Data Warehousing

Spark can process data across multiple computers (clusters) much faster than traditional systems.

## Why Use Spark?

Imagine you have:
 - Excel → handles thousands of rows
 - Pandas → handles millions of rows
 - Spark → handles billions of rows

Spark distributes work across multiple machines.

### Traditional Processing
```
Machine 1
  |
  ---> Data Processing
```

### Spark Processing
```
Machine 1
Machine 2
Machine 3
Machine 4

All process data simultaneously
```

## Core Components
- Spark Core
- Spark SQL
- Spark Streaming
- MLlib
- GraphX

## Installing Spark
```bash
# macos
# 1. Install Java (required to run Apache Spark)
brew install openjdk@17

# 2. Install Apache Spark
brew install apache-spark

# 3. Install PySpark via pip
pip install pyspark

java --version

echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.zshrc
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.3.1/libexec
source ~/.zshrc
echo $SPARK_HOME

spark-submit --version
pyspark --version

```

### Creating Your first Spark Session
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StudentTutorial").getOrCreate()

print("Spark Started")

```

### Spark Dataframe
- very similar to a pandas DataFrame but distributed
```python

data = [
    ("John", 22),
    ("Mary", 25),
    ("Peter", 30)
]

df = spark.createDataFrame(data, ["Name", "Age"])

df.show()


df = spark.read.csv(
    "students.csv",
    header=True,
    inferSchema=True
)

df.show()


```

### Run spark job
```bash
# pyspark
docker run -it apache/spark /opt/spark/bin/pyspark

# Start an interactive PySpark session
docker run -it --rm \
  --name pyspark \
  -p 4040:4040 \
  -v $(pwd)/spark-apps:/opt/spark-apps/ \
  apache/spark:3.5.1 \
  /opt/spark/bin/pyspark --master local[*]

# scala
docker run -it apache/spark /opt/spark/bin/spark-shell

# Run Spark shell interactively in local mode

docker run -it --rm \
  --name spark-shell \
  -p 4040:4040 \
  apache/spark:3.5.1 \
  /opt/spark/bin/spark-shell --master local[*]


# run pyspark script
docker cp spark-apps/1_main.py spark-master:/opt/spark-apps/
docker exec -it spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark-apps/1_main.py


# Copy the script into the master container and submit it
docker cp spark-apps/1_main.py spark-master:/opt/spark/work-dir/
docker exec spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark/work-dir/1_main.py


docker run -it --rm \
  -p 8888:8888 \
  -p 4040:4040 \
  -v $(pwd):/home/jovyan/work \
  jupyter/pyspark-notebook


version: '3.8'

services:
  spark-jupyter:
    image: jupyter/pyspark-notebook:latest
    container_name: pyspark_jovyan
    restart: always
    environment:
      - JUPYTER_ENABLE_LAB=yes
    ports:
      - "8888:8888"   # Jupyter Lab
      - "4040:4040"   # Spark UI
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./data:/home/jovyan/data

```



## References
- https://oneuptime.com/blog/post/2026-02-08-how-to-run-apache-spark-in-docker/view
- https://medium.com/@sanjeets1900/setting-up-apache-spark-from-scratch-in-a-docker-container-a-step-by-step-guide-2c009c98f2a7
- https://github.com/experientlabs/spark-dp-101/tree/main
- https://spark.apache.org/docs/latest/index.html