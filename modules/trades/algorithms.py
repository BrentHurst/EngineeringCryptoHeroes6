#!/usr/bin/env python3

from db.database import *

class trade():
    def __init__(self, coinFrom, coinTo, amt, exchange):
        self.coinFrom = coinFrom
        self.coinTo = coinTo
        self.amount = amt
        self.exchange = exchange

def value_averaging(poolID):
    trades = []
    with coindb() as db:
        coins = db.getPoolCoins(poolID)
        values = {}
        for c,v in coins.items():
            values[c] = v * db.getCurrentValue(c, "gdax")
        s = sum(coins.values()) / len(coins)
        for c,v in coins.items():
            if c != "USD":
                trades.append(Trade(c, "USD", v - s, "gdax"))
        return trades


