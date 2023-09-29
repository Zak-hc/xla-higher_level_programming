#!/usr/bin/python3
"""lklkkkl"""
import requests

a = requests.get('https://alx-intranet.hbtn.io/status')
x = a.text
print("Body response:")
print("\t- type:", type(x))
print("\t- content:", x)
