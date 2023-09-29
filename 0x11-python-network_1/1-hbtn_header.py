#!/usr/bin/python3
# displays dvalue of  X-Request-Id variablein the headeroftheresponse
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as rep:
    body = rep.info()
    i = 'X-Request-Id'
    if i in body:
        store = body[i]
        print(store)
    else:
        print('desole')
