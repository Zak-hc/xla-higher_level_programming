#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as rep:
    body = rep.read()
    utf = body.decode('utf-8')
print("Body response:")
print("  - type:", type(body))
print("  - content:", body)
print("  - utf8 content:", utf)
