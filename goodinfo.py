#!/usr/bin/env python

import psycopg2
from StockInfo import stockinfo
import sys
improt time

conn = psycopg2.connect(database="stockdb", user="yfwu", password="amigo", host="127.0.0.1", port="5432")
cur = conn.cursor()

def insert(info):
    for year in list(info.data.keys()):
        command = "INSERT INTO StockInfo(No, Date, Price) VALUES ({no}, '{date}',{price})".format(no = ID, date = date, price = temp[(year, month)].data[index])
        cur.execute(command)


for line in open(sys.argv[1], 'r'):
    ID = line.replace('\n', '')
    try:
        obj = stockinfo(ID)
        insert(obj)
    except:
        time.sleep(1200)
        obj = stockinfo(ID)
        insert(obj)

    conn.commit()
    time.sleep(30)

conn.close()
