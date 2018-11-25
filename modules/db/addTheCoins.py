#!/usr/bin/env python3

from database import *

print('hi')
with coindb() as db:
    print(db.getCoinByID('%'))
    db.addCoin('BTC')
    print(db.getCoinByID('%'))
    print(db.getCoinIDByName('BTC'))

