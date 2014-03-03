#!/usr/bin/env python
import urllib.request

hdr = {'User-Agent': 'Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


 # establish webpage connection
def urlopen(url):
    req = urllib.request.Request(url, headers=hdr)
    return urllib.request.urlopen(req)
