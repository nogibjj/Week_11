#!/usr/bin/python

import sqlite3

# establishing connection
conn = sqlite3.connect("test.db")
# creating table
conn.execute(
    """CREATE TABLE COMPANY
         (ID INT PRIMARY KEY,
         NAME TEXT    NOT NULL,
         AGE INT     NOT NULL,
         ADDRESS  CHAR(50),
         SALARYn REAL);"""
)

# closing connection
conn.close()
