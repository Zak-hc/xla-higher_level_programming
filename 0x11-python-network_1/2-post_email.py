#!/usr/bin/python3
"""script takesinURL and an emailsendsPOSTrequest tothepassed URL withmail"""
import sys
import urllib.request

if __name__ == "__main__":
    email = sys.argv[2]
    cnvr = email.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data=cnvr, method='POST')
    with urllib.request.urlopen(req) as rep:
        store = rep.read().decode('ascii')
        print(store)
