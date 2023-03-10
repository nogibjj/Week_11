#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("test.db")
# opened database successfully

conn.execute(
    "INSERT OR REPLACE INTO COMPANY (ID, NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Jeremy', 32, 'California', 20000.00 )"
)

conn.execute(
    "INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
)

conn.execute(
    "INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
)

conn.execute(
    "INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
)

conn.commit()
print("Records created successfully")
conn.close()
