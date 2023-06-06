#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ma7souba = abs(number) % 10
if number > 0 or number == 0:
    if ma7souba > 5:
        print(f"last digit of {number} is {ma7souba} and is greater than 5")
    elif ma7souba == 0:
        print(f"last digit of {number} is {ma7souba} and is 0")
    else:
        print(f"last digit of {number} is {ma7souba} and is less than 6 and not 0")
else:
    print(f"last digit of {number} is {-ma7souba} and is less than 6 and not 0")
