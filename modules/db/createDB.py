#!/usr/bin/env python3

from db.database import *

with coindb() as db:
    db.construct()
