#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = " + str(row[0]))
    print("NAME = " + str(row[1]))
    print("ADDRESS = " + str(row[2]))
    print("SALARY = " + str(row[3]))


conn.close()
