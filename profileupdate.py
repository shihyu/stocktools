#!/usr/bin/env python

import psycopg2
from DatePrice import dateprice
import sys

conn = psycopg2.connect(database="stockdb", user="yfwu", password="amigo", host="127.0.0.1", port="5432")
cur = conn.cursor()

for line in open(sys.argv[1], 'r'):
    num = line.strip('\n').split(',')[0]
    name = line.strip('\n').split(',')[1]
    command = "INSERT INTO Profile(MarketNo, MarketName) VALUES ({num}, '{name}')".format(num = num, name = name)
    print(command)
    cur.execute(command)

conn.commit()
conn.close()
