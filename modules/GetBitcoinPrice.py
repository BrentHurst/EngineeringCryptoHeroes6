#!/usr/bin/env python3
import requests

BitcoinPriceUrl = 'http://api.coindesk.com/v1/bpi/currentprice.json'

def BitcoinPrice():
    return requests.get(BitcoinPriceUrl).json()['bpi']['USD']['rate_float']

if __name__ == "__main__":
    print(BitcoinPrice())
