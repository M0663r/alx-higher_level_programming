#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
numList = [int(digit) for digit in str(number)]

print(f'Last digit of {number} is {numList[-1]} and is', end=" ")
if numList[-1] == 0:
    print("0")
elif numList[-1] > 5:
    print("greater than 5")
elif numList[-1] < 6 and numList[-1] != 0:
    print("less than 6 and not 0")
