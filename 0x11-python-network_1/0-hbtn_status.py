#!/usr/bin/python3
import urllib.request
if __name__ == '__main__':
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as rep:
        body = rep.read()
        utf = body.decode('utf-8')
        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", utf)
