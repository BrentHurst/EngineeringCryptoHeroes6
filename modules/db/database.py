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
        c.execute("INSERT INTO coins VALUES (?)", coin_name)

