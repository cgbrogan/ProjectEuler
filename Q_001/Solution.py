#!/usr/bin/python

s = []
for val in range(0,1000):
    if (val % 3 == 0) and (val not in s):
        s.append(val)
    elif (val % 5 == 0) and (val not in s):
        s.append(val)
    else:
        continue

print sum(s)

# Answer: 233168
