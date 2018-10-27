#!/usr/bin/env python3

from database import *

with coindb() as db:
    db.construct()
