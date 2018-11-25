#!/usr/bin/env python3

from db.database import *





             # test getIncompleteTrades()
             # test markTradeComplete()

             # amount is in usd

def maketrades():
    with coindb() as db:
        todo = db.getIncompleteTrades()
        for tradeID, tradePoolID, coinFrom, coinTo, amount, exchangeID, completed in todo:
            coinFromVal = db.getCurrentValue(coinFrom, exchangeID)
            coinToVal = db.getCurrentValue(coinTo, exchangeID)

            # TradingPoolCoinData.coinAmount -= amount / coinFromVal
            # TradingPoolCoinData.coinAmount += amount / coinToVal
            # TradingPools.value = sum(all coins on their max exchange)
            db.updateCoinAmount(tradePoolID,amount,coinFrom,coinTo,coinFromVal,coinToVal)

            db.markTradeComplete(tradeID)
