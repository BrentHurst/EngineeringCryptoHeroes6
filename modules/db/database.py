#!/usr/bin/env python3

import sqlite3
import os

class coindb():
    def __init__(self, name="ech6.db"):
        self.connection = sqlite3.connect(name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.connection.commit()
        self.connection.close()
        return True

    def construct(self, filename=""):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if not filename:
            filename = os.path.join(dir_path, "createDB.sqlite")

        c = self.connection.cursor()

        with open(filename, "r") as f:
            c.executescript(f.read())

    def cursor(self):
        return self.connection.cursor()

    def updateMarketState(self,coinID,exchangeID,value):
        c = self.connection.cursor()
        c.execute("insert into cryptoData values (?, ?, ?, CURRENT_TIMESTAMP)",(coinID,exchangeID,value))

    def getIncompleteTrades(self):
        c = self.connection.cursor()
        return c.execute("select rowid, * from trades where completed = 0").fetchall()

    def getCurrentValue(self,coin,exchange):
        c = self.connection.cursor()
        return c.execute("select value from cryptoData where coinID=? and exchangeID=? order by timestamp desc limit 1",(coin,exchange)).fetchall()[0][0]

    def markTradeComplete(self,tradeID):
        c = self.connection.cursor()
        c.execute("update trades set completed = 1 where rowid = ?",tradeID)

    def updateCoinAmount(self,tradePoolID,amount,coinFrom,coinTo,coinFromVal,coinToVal):
        c = self.connection.cursor()
        c.execute("update tradingPoolCoinData set coinAmount = (coinAmount - (? / ?)) where tradingPoolID = ? and coinID = ?",(amount,coinFromVal,tradePoolID,coinFrom))
        c.execute("update tradingPoolCoinData set coinAmount = (coinAmount + (? / ?)) where tradingPoolID = ? and coinID = ?",(amount,coinToVal,tradePoolID,coinTo))

        exchanges = ['gdax','bitstamp','binance']
        d = {'BTC':-1,'LTC':-1,'ETH':-1}
        for key in d:
            for ex in exchanges:
                val = self.getCurrentValue(key,ex)
                if val > d[key]:
                    d[key] = val

        rows = c.execute("select coinID, coinAmount from tradingPoolCoinData where tradingPoolID = ?",tradePoolID).fetchall()

        s = 0
        for coin,coinamt in rows:
            s += d[coin] * coinamt

        c.execute("update tradingPools set value = ? where rowid = ?",(s,tradePoolID))
