#!/usr/bin/env python

import urllib
import re
import time
import sys

tmp = open("stock.list").read()
tickers = tmp.split("\n")

delay = 1
if len(sys.argv) > 1:
    delay = sys.argv[1]

tickers.append("^dji")
tickers.append("^ixic")

while True:
    price = []
    row = []
    c = 1
    for t in tickers:
        if len(t.strip()) < 1:
            continue
        url = "http://finance.yahoo.com/q?"
        param = urllib.urlencode({'s': t})
        #print param
        uh = urllib.urlopen(url + "%s" % param)
        html = uh.read()
        pat = re.compile('yfs_l10_' + t.strip() + '">(\d*,*\d+\.\d+)</span>')
        rlt = pat.search(html)
        if rlt:
             price.append(t + ":" + rlt.group(1))
             row.append(t + ":" + rlt.group(1))
             c %= 3
             #print c
             if c == 0:
                 print "\t".join(row)
                 row = []
        c += 1
    print "\t".join(row)
    time.sleep(int(delay))
    #result = "\n".join(price)
    #output = open("stock.result", "w")
    #output.write(result)
    #output.close()
    print '-' * 30
    #time.sleep(30)
    
