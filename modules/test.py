#!/usr/bin/env python3

from db.database import *
from marketstate.gatherMarketState import *

with coindb() as db:
    db.construct()

gatherMarketState()


