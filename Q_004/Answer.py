#!/usr/bin/python
prod = 0
pdrome = []

for aProd in xrange(100, 1000):
    for bProd in xrange(100, 1000):
        prod = aProd *  bProd
        if str(prod) == str(prod)[::-1]:
            pdrome.append(prod)

print max(pdrome)


# Answer: 906609
