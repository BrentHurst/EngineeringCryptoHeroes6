#!/usr/bin/env python3

from database import *


def maketrades():
    with coindb() as db:
        todo = db.getIncompleteTrades()
        for tradeID, tradePoolID, coinFrom, coinTo, amount, exchangeID, completed in todo:
             coinFromVal = db.getCurrentValue(coinFrom, exchangeID)
             coinToVal = db.getCurrentValue(coinTo, exchangeID)

             #update the pool coin data

             db.markTradeComplete(tradeID)



