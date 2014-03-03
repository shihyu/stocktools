#!/usr/bin/env python

import psycopg2
from DatePrice import dateprice
import sys
import time

conn = psycopg2.connect(database="stockdb", user="yfwu", password="amigo", host="127.0.0.1", port="5432")
cur = conn.cursor()

def insert(ID):
    temp = {}
    for year in range(2009, 2014):
        for month in range(1, 13):
            year = str(year)
            month = str(month)
            temp[(year, month)] = dateprice(ID, year, month)

            for index in list(temp[(year, month)].data.keys()):
                date = str(year + '/' + month + '/' + index[-2:])
                command = "INSERT INTO DatePrice(No, Date, Price) VALUES ({no}, '{date}',{price})".format(no = ID, date = date, price = temp[(year, month)].data[index])
                print(command)
                cur.execute(command)
        conn.commit()

for line in open(sys.argv[1], 'r'):
    ID = line.replace('\n', '').split(',')[0]
    try:
        insert(ID)
        time.sleep(60)
    except:
        print(ID + ' Error!')
        time.sleep(600)
        insert(ID)

conn.close()
