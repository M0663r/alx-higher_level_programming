#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            print("{:02d}, {:02d}".format(i, j), end=', ' if not (i == 8 and j == 9) else '\n')
