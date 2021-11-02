# Akhil Havaldar; ash2sfp

import json
import pandas as pd
import sqlite3
import argparse
import requests
import time
import csv
from csv import writer


# Choosing which stock to get information from
stock = input("Enter Stock Ticker: ")

# Defining the key and URL
apikey = "AToTpREVIw55N3JNY5otS66TdWPPfqNMKAeWP0e7"
url = "https://yfapi.net/v6/finance/quote"

# Getting the stock info from the API
querystring = {"symbols":stock}
headers = {
  'x-api-key': apikey
   }
response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
stock_json = response.json()

# Converting the time into readable format
timestamp = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))

# Printing the resulting stock data
result = ("Company Name: " + str(stock_json['quoteResponse']['result'][0]["shortName"]) +
      " Price: $" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) +
      " Market Time: " + real_time)
print(result)

# Storing the stock data in a list
list = [str(stock_json['quoteResponse']['result'][0]["symbol"]),
        real_time, str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])]


# Writing the stock data from the list to a csv file
with open('yahoo_api_req.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(list)
    f_object.close()

