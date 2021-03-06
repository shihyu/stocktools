#!/usr/bin/env python

from DatePrice import dateprice
from StockInfo import stockinfo
import sys
import time


with open(sys.argv[2] + '.csv', 'w', newline='') as fp:
    for line in open(sys.argv[1], 'r'):
        ID = line.strip('\n')
        print(ID)
        temp_start = dateprice(ID, '2011', '1')
        temp_end = dateprice(ID, '2014', '1')
        start = list(temp_start.data.keys())
        start.sort()
        end = list(temp_end.data.keys())
        end.sort()
        x = float(temp_start.data[start[0]])
        y = float(temp_end.data[end[0]])
        print(str(x) + ' & ' + str(y))
        info = stockinfo(ID)
        m = {}
        n = {}
        for index, element in enumerate(['2011', '2012', '2013']):
            m[index + 1] = float(info.data[element]['CashDividendTotal'])
            n[index + 1] = float(info.data[element]['StockDividendTotal'])

        print(str(m) + ' & ' + str(n))
        result = ((y * (1 + n[1] / 10) * (1 + n[2] / 10) * (1 + n[3] / 10)) + (m[1] + m[2] * (1 + n[1] / 10) + m[3] * (1 + n[1] / 10) * (1 + n[2] / 10))) / x
        fp.write(str([int(ID), m[1], m[2], m[3], n[1], n[2], n[3], x, y, result])[1:-1] + '\n')
        time.sleep(2)
