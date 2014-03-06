#!/usr/bin/env python

#Get Web Source
import urllib.request

hdr = {'User-Agent': 'Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Establish Connection
def urlopen(url):
    req = urllib.request.Request(url, headers=hdr)
    return urllib.request.urlopen(req)

import sys

ID = int(sys.argv[1])
source = 'http://www.goodinfo.tw/stockinfo/StockDividendSchedule.asp?STOCK_ID='
result = urlopen(source + str(ID)).read().decode('utf8')


# Parse Data from Web Source
from lxml import etree

parse_tree = etree.HTML(result)

data_table_1 = parse_tree.xpath("//table//table//table[5]//tr[@bgcolor='white']")
data_table_2 = parse_tree.xpath("//table//table//table[5]//tr[@bgcolor='#e7f3ff']")
total = data_table_1 + data_table_2
data = {}
infolist = ['SurplusYear',
            'DividendYear',
            'ShareholdersMeeting',
            'ExDividendDate',
            'ExDividendPrice',
            'ExRightsDate',
            'ExRightsPrice',
            'PriceStaticsticsHighest',
            'PriceStaticsticsMinium',
            'PriceStaticsticsAverage',
            'CashDividendSurplus',
            'CashDividendProvident',
            'CashDividendTotal',
            'StockDividendSurplus',
            'StockDividendProvident',
            'StockDividendTotal',
            'TotalDividend',
            'AnnualYield']
for item in total:
    temp = {}
    for index, element in enumerate(item):
        temp[infolist[index]] = element.text
    data[item[1].text] = temp


# Write Data To PostgreSQL Database
import psycopg2

conn = psycopg2.connect(database="stockdb", user="yfwu", password="amigo", host="127.0.0.1", port="5432")
cur = conn.cursor()

sen_1 = "INSERT INTO StockInfo("
sen_2 = ") VALUES ("
sen_3 = ");"
for index_data in list(data.keys()):
    raw_key = "No,"
    raw_value = str(ID) + ","
    year = data[index_data]
    
    def none_null(text):
        return "Null" if text == "None" else text
    
    for index_year in list(year.keys()):
        key = index_year
        raw_key += none_null(str(key)) + ","
        value = year[index_year]
        raw_value += none_null(str(value)) + ","
    print(sen_1 + raw_key + sen_2 + raw_value + sen_3)
    cur.execute(sen_1 + raw_key[:-1] + sen_2 + raw_value[:-1] + sen_3)
conn.commit()