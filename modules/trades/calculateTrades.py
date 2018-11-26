#!/usr/bin/env python3

from db.database import *
import algorithms

def calculateTrades():
    with coindb() as db:
        pools = db.getPools()
        for pool in pools:
            poolID, algorithmID, agressiveness, value = pool
            algorithm = db.getAlgorithmByID(algorithmID)
            algorithmID, algorithmName, agressiveness = algorithm

            trades = algorithms.__dict__[algorithmName](poolID)

            for trade in trades:
                db.createTrade(poolID, trade.coinFrom, trade.coinTo, trade.amount, trade.exchange)

if __name__ == "__main__":
    calculateTrades()

