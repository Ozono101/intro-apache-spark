#!/bin/bash

spark-submit --master 'local[*]' --executor-memory 1G --driver-memory 1G 2_main.py

# spark-submit --master 'local[3]' --num-executors 2 --driver-cores 2 2_main.py

# spark-submit --master 'local[3]' --num-executors 2 --driver-cores 2 /usr/local/spark/examples/src/main/python/pi.py 10