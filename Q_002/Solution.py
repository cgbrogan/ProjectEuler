#!/usr/bin/python

first = 1
second = 2
counter = 2

while (True):
    if second >= 4000000:
        break
    else:
        second, first = first + second, second
        if (second % 2 == 0):
            counter += second

print counter

#Answer: 4613732
