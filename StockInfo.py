#!/usr/bin/env python
import re
from liburlopen import urlopen
from lxml import etree


class stockinfo:
    def __init__(self, ID):
        # Get the webpage's source html code
        source = 'http://www.goodinfo.tw/stockinfo/StockDividendSchedule.asp?STOCK_ID='
        result = urlopen(source + str(ID)).read().decode('utf8')

        parse_tree = etree.HTML(result)

        data_table_1 = parse_tree.xpath("//table//table//table[5]//tr[@bgcolor='white']")
        data_table_2 = parse_tree.xpath("//table//table//table[5]//tr[@bgcolor='#e7f3ff']")
        total = data_table_1 + data_table_2
        self.data = {}

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
            self.data[item[1].text] = temp
            print(temp)
