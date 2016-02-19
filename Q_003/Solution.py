#!/usr/bin/python

potential_val = 2
number = 600851475143
pfList = []

while True:
    potential_val
    if (float(number) / float(potential_val) == 1.0):
        pfList.append([number, potential_val])
        break
    elif (number % potential_val == 0):
        pfList.append([number, potential_val])
        number = number / potential_val
        continue
    else:
        potential_val += 1
        continue

print pfList

# Answer: 6857
