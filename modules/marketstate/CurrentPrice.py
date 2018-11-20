#!/usr/bin/env python3

# functions for crypto data

import requests

def GetCurPrice(symbol,exchange):
    validsymbols = ('BTCUSD','LTCUSD','ETHUSD')
    validexchanges = ('gdax','bitstamp','binance')

    if symbol not in validsymbols:
        raise ValueError(symbol,'is not in the list of valid symbols:',validsymbols)
    if exchange not in validexchanges:
        raise ValueError(exchange,'is not in the list of valid symbols:',validexchanges)

    if exchange == 'binance':
        symbol += 'T'

    url = 'https://apiv2.bitcoinaverage.com/exchanges/ticker/' + exchange

    return requests.get(url).json()['symbols'][symbol]['last']


if __name__=='__main__':
    raise Exception('Why are you calling this file?')
