#!/usr/bin/python

sumSquared = sum([x**2 for x in xrange(0,101)])
squaredSum = sum([x for x in xrange(0,101)]) ** 2

print squaredSum - sumSquared

# Answer = 25164150
