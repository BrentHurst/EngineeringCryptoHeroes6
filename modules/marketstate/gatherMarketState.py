#!/usr/bin/env python3

from CurrentPrice import *
from db.database import *


def gatherMarketState():
    exchanges = ['gdax','bitstamp','binance']
    symbols = ['BTC','LTC','ETH']

    with coindb() as db:
        for ex in exchanges:
            for sym in symbols:
                symusd = sym + 'USD'
                curprice = GetCurPrice(symusd,ex)
                db.updateMarketState(sym,ex,curprice)



if __name__ == "__main__":
    gatherMarketState()
