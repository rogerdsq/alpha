#!/usr/bin/env python

import urllib
import re
import time
import sys
import os


def connected_to_net():
    if os.system("/bin/ping www.yahoo.com -c 2 >/dev/null 2>&1") == 0:
        return True
    else:
       print "sleep"
       time.sleep(120)
       return False

tmp = open("stock.list").read()
tickers = tmp.split("\n")
tickers.sort()

delay = 1
if len(sys.argv) > 1:
    delay = sys.argv[1]

tickers.append("INDEXDJX:.DJI")
tickers.append("INDEXNASDAQ:.IXIC")


while connected_to_net():
    row_price = []
    row_change = []
    c = 1
    print '-' * 9 + ' ' + time.asctime() + ' ' + '-' * 9
    for t in tickers:
        if len(t.strip()) < 1:
            continue
        try:
            url = "http://www.google.com/finance?"
            param = urllib.urlencode({'q': t})
            #print param
            uh = urllib.urlopen(url + "%s" % param)
            #uh = urllib.urlopen(url + yhoo')
            html = uh.read()
            #print html
            pat = re.compile('ref_\d+_l">(\d*,*\d+\.\d+)</span>')
            rlt = pat.search(html)
            if rlt:
                row_price.append((t[-4:] + ":" + rlt.group(1)).rjust(13))
            pat = re.compile('ref_\d+_cp">(\([-+]?\d+\.\d+%\))</span>')
            rlt = pat.search(html)
            if rlt:
                row_change.append(rlt.group(1).rjust(13))
                c %= 3
                #print c
                if c == 0:
                    print "  ".join(row_price)
                    print "  ".join(row_change)
                    row_price = []
                    row_change = []
        except:
            continue
        c += 1
    if row_price:
        print "\t".join(row_price)
        print "\t".join(row_change)
    time.sleep(int(delay))
    #result = "\n".join(price)
    #output = open("stock.result", "w")
    #output.write(result)
    #output.close()
    #time.sleep(30)
    
