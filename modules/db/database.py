#!/usr/bin/env python3

import sqlite3

class coindb():
    def __init__(self, name="ech6.db"):
        self.connection = sqlite3.connect(name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print(locals())
        self.connection.commit()
        self.connection.close()
        return True

    def construct(self, filename="createDB.sqlite"):

        c = self.connection.cursor()

        with open(filename, "r") as f:
            c.executescript(f.read())

    def cursor(self):
        return self.connection.cursor()

    def addCoin(self, coin_name):
        c = self.connection.cursor()
        c.execute("INSERT INTO coins VALUES (?)", (coin_name,))

    def getCoinByID(self, coinID):
        c = self.connection.cursor()
        return c.execute("SELECT * FROM coins WHERE coinID=?", (coinID,))

    def getIncompleteTrades(self):
        c = self.connection.cursor()
        return c.execute("SELECT * FROM trades WHERE completed=0")

    def getCurrentValue(self, coinID, exchangeID):
        c = self.connection.cursor()
        return c.execute("SELECT value FROM cryptoData WHERE coidID=? AND exchangeID=? ORDER BY timestamp DESC LIMIT 1", (coinID, exchangeID))[0]

    def markTradeComplete(self, tradeID):
        c = self.connection.cursor()
        c.execute("UPDATE completed=1 WHERE tradeID=?", (tradeID,))







