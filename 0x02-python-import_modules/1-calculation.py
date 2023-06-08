#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    add = add(a, b)
    print(f"{a} + {b} = {add}")
    sub = sub(a, b)
    print(f"{a} - {b} = {sub}")
    mul = mul(a, b)
    print(f"{a} * {b} = {mul}")
    div = div(a, b)
    print(f"{a} / {b} = {div}")
