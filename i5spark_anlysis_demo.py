import findspark

findspark.init()
# A simple demo for working with SparkSQL and vehicless
import pyspark
from pyspark.sql import SparkSession
import json
import sys
import time
from termcolor import colored

import random
import argparse
from datetime import date
import calendar
import os
import datetime



def count_files_in_folder(path):

    dirListing = os.listdir(path)

    file_count = len(dirListing)
    return file_count

def data_anlysis():

    inputFile =  r"data/vehicles.csv"
    

    # inputFile = 'tesvehicles.json'
    spark = SparkSession.Builder().appName('VH').getOrCreate()
    df = spark.read.csv(inputFile)

    print("Loading vehicles from " + inputFile)

    # prev_count = count_files_in_folder(inputPath)
    # input = hiveCtx.read.json(inputFile)
    # input.registerTempTable("vehicles")
    topvehicless = df.show()
    print(topvehicless)

    print(colored("2. filter out now span data:", "blue", attrs=["reverse", "blink"]))
    print('schema:')
    print(df.printSchema())




if __name__ == "__main__":
    data_anlysis()
    # python3 i5spark_anlysis.py
