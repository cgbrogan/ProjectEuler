#!/usr/bin/python
prod = 0
pdrome = []

#print(max(a * b for a in range(100, 1000) for b in range(a, 1000) if str(a * b) == str(a * b)[::-1]))

for aProd in xrange(100, 1000):
    for bProd in xrange(100, 1000):
        prod = aProd *  bProd
        if str(prod) == str(prod)[::-1]:
            pdrome.append(prod)

print max(pdrome)


# Answer: 906609
