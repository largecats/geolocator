##################################################
#               Importing modules                #
##################################################
import re
import pandas as pd
import numpy as np
import csv
import time
from time import sleep
import random
import googlemaps
import os

##################################################
#                   prep work                    #
##################################################
# set working directory
path = ""
os.chdir(path)
API_key = ""
inputFileName = "addresses.csv"
outputFileName = "coordinates.csv"
pauseTime = [1,3]

# set up locator
geolocator = googlemaps.Client(key = API_key)

# set up output file
with open(outputFileName, 'w', encoding = 'UTF-8', newline = "") as outputFile:
  colNames = ['addresses', 'coordinates']
  writer = csv.writer(outputFile)
  writer.writerow(colNames)

##################################################
#                helper functions                #
##################################################
def read_csv_into_list(fileName):
  data = []
  with open(fileName, 'r', encoding = 'UTF-8') as f:
    for row in f:
      row = row.strip()
      data.append(row)
      print(row)
  data.pop(0)
  return data

##################################################
#                   main work                    #
##################################################
# read in addresses
addressList = read_csv_into_list(inputFileName)

for address in addressList:
  # pause the loop for a random amount of time
  sleep(random.randint(pauseTime[0], pauseTime[1]))
  location = geolocator.geocode(address)
  try:
    # record latitude and longitude
    coordinates = (location[0]['geometry']['location']['lat'], location[0]['geometry']['location']['lng'])
  except:
    coordinates = "NA"
  print(coordinates)
  with open(outputFileName, 'w', encoding = 'UTF-8', newline = "") as outputFile:
    data = [address, coordinates]
    print(data)
    writer = csv.writer(outputFile)
    writer.writerow(data)