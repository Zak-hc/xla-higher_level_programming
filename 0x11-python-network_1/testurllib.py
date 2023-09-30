#!/usr/bin/python3
import urllib.request
p=urllib.request.urlopen("https://alx-intranet.hbtn.io/status")
print(p)
print(p.info())
print(p.read().decode('utf-8'))
