#!/usr/bin/env python
from lxml import etree
from liburlopen import urlopen


class dateprice:
    def __init__(self, ID, year, month):
        # Get the webpage's source html code
        # ID / Month / Year must be string
        if len(month) == 1:
            month = '0' + month
        source = "http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY_AVG/genpage/Report{year}{month}/{year}{month}_F3_1_8_{ID}.php?STK_NO={ID}&myear={year}&mmon={month}".format(ID=ID, year=year, month=month)
        html = str(urlopen(source).read())

        # parse the html source tree
        parse_tree = etree.HTML(html)
        date_price = parse_tree.xpath("//table//table//table[6]//td//text()")[4:-2]

        # turn data into dictionary
        self.data = dict(zip(date_price[0::2], date_price[1::2]))
