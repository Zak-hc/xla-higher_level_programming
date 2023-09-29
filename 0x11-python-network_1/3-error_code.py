#!/usr/bin/python3
""""ggg"""
import urllib.request
import sys
from urllib.error import HTTPError
try:
    with urllib.request.urlopen(sys.argv[1]) as req:
        for i in req:
            if req[i] == 200:
                print("Index")
except HTTPError as err:
    print("Error code: " ,err.code)

