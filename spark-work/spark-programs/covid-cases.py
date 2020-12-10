import argparse
import pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from datetime import date, timedelta, datetime
import time
import csv

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

spark = SparkSession \
		.builder \
		.appName("covid-cases") \
		.getOrCreate()

#Task1: read in csv data without a customized schema
#source file: us_confirmed_pcs.csv
def loadDataTask(infile,outfile)
    start_time=time.time()
    df = spark.read.option("header",True).option("inferSchema",True)\
        .csv(infile)
    df = df.withColumn("Date_parse",df["Date"].cast('date')).drop('Date')
    df = df.withColumn('month',month(to_timestamp('Date_parse','MM/dd/yyyy'))).drop('Date_parse')

    sum_col = df.columns[0:-1]w
    results= df.groupBy("month").agg(*[sum(df[c_name]) for c_name in sum_col])
    results.sort("month").coalesce(1).write.csv(outfile)
    end_time = time.time()
    return (end_time - start_time)

# Task2: Read in the transpose of the output dataframe in task 1, aggregate
# source file: covid_2.csv
def aggDataTask(infile,outfile):
    start_time=time.time()
    df2 = spark.read.option("header",True).option("inferSchema",True).csv(infile)
    sum_col2 = df2.columns[1:]
    results= df2.groupBy('0').agg(*[sum(df2[c_name]) for c_name in sum_col2])
    results.sort("0").coalesce(1).write.csv(outfile)
    end_time = time.time()
    return (end_time - start_time)

loadDataTime = loadDataTask(parsed_args.input,parsed_args.output)
#aggDataTime = aggDataTask(parsed_args.input,parsed_args.output)