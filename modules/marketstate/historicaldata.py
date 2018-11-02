#!/usr/bin/env python3

# functions for historical crypto data

import requests
from os import system

url_array = []
url_array.append('https://apiv2.bitcoinaverage.com/indices/global/history/')
url_array.append('?period=')
url_array.append('&format=')

# Don't use these helper functions
def ____MakeURLString(s):
    return url_array[0] + s + url_array[1] + 'alltime' + url_array[2] + 'csv'

def ____GetTheJson(s):
    return requests.get(____MakeURLString(s)).text
# Don't use the above helper functions



#### Use the functions below this line ####


def HistoricalBitcoinPrice():
    return ____GetTheJson('BTCUSD')

def HistoricalEtheriumPrice():
    return ____GetTheJson('ETHUSD')

def HistoricalLitecoinPrice():
    return ____GetTheJson('LTCUSD')

if __name__ == "__main__":
    print("Why did you run this file?")
