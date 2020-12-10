import argparse
import pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from datetime import date, timedelta, datetime
import time


def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-i", "--input", help="input file")
    parser.add_argument ("-o", "--output", default="result.csv", help="output file default result.csv")
    # parse the args
    args = parser.parse_args ()

    return args

parsed_args = parseCmdLineArgs ()
print(parsed_args)

start_time=time.time()
spark = SparkSession \
		.builder \
		.appName("flight") \
		.getOrCreate()

schema = StructType([ \
    StructField("Date", DateType(),True), \
    StructField("AirportName", StringType(), True), \
    StructField("PercentOfBaseline", FloatType(), True), \
    StructField("City", StringType(), True), \
    StructField("State", StringType(), True), \
    StructField("Country", StringType(), True), \
  ])


df = spark.read.load(parsed_args.input, format="csv",sep=",",schema=schema)
df = df.withColumn('month',month(to_timestamp('Date','yyyy/MM/dd')))

df.printSchema()
df.limit(1).show()

# exprs = df.columns
results = df.groupBy("month","AirportName","City","State","Country").agg(avg("PercentOfBaseline"))
results.sort("month","AirportName").coalesce(1).write.csv('file:///work/covid-flight.csv')


end_time = time.time()
