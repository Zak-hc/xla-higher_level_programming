#!/usr/bin/python3
""""ggg"""
import urllib.request
import sys
from urllib.error import HTTPError
try:
    with urllib.request.urlopen(sys.argv[1]) as req:
              a = req.read().decode("utf-8")
              print(a)
except HTTPError as err:
    print("Error code: ", err.code)
