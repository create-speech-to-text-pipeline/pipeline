from pyspark.sql import SQLContext, HiveContext, SparkSession
import pyspark
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('SparkApp').setMaster('yarn')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.appName('SparkApp').getOrCreate()

# **modify this file with code from nahom

# read data from bucket (and/or database?)
curr_dframe = spark.read.option("header", True).csv(
    "/mnt/10ac-batch-6/bucket/orig_db.csv")

# curr_dframe = spark.read.option("header", True).csv(
#     "/mnt/10ac-batch-6/bucket/netflix_titles.csv")

# perform transformations/fiters
curr_dframe_filtered = curr_dframe.filter(
    curr_dframe['uuid'] == '0001') # a transformed row, for example

# write data back into s3 bucket
curr_dframe_filtered.write.option("header", True).csv(
    "/mnt/10ac-batch-6/bucket/transformed_db.csv")

# curr_dframe_filtered.write.option("header", True).csv(
#     "/mnt/10ac-batch-6/bucket/transformed_db.csv")
