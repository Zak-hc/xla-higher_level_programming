#!/usr/bin/python3
""""ggg"""
import urllib.request
import sys
from urllib.error import HTTPError
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            a = req.read().decode("UTF-8")
            print(a)
    except HTTPError as err:
        print(f"Error code: {err.code}")
