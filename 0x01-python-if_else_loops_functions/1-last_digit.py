#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = abs(number) % 10
if number > 0 or number == 0:
    if m > 5:
        print(f"Last digit of {number} is {m} and is greater than 5")
    elif m == 0:
        print(f"Last digit of {number} is {m} and is 0")
    else:
        print(f"Last digit of {number} is {m} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {-m} and is less than 6 and not 0")
