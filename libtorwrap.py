#! /usr/bin/env python
 
import urllib.request

def urlopen(url):
    proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:9666'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    return urllib.request.urlopen