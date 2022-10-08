#!/bin/sh
  
echo "calling spark script"
export HADOOP_USER_NAME=hdfs
spark-submit --driver-memory 2g --executor-memory 2g --executor-cores 2 --num-executors 2 --deploy-mode cluster spark_transformation.py