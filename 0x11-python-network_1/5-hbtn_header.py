#!/usr/bin/python3                                                       
"""lklkkkl"""                                                            
import requests                                                          
import sys                                                           
if __name__ == "__main__":
    x = requests.get(sys.argv[1])                  
    i = 'X-Request-Id'
    stor = x.headers.get(i)
    print(stor)
