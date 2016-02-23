#!/usr/bin/python

a = 999
b = 999
bol = False
pdrome = []

for aProd in xrange(a, 100, -1):
    for bProd in xrange(b, 100, -1):
        prod = aProd * bProd
        if len(str(prod)) == 5:
            if str(prod)[0:2] == str(prod)[4:2:-1]:
                print prod
                pdrome.append(prod) 
                print pdrome
                bol = True
                break
        else:
            if str(prod)[0:3] == str(prod)[5:2:-1]:
                pdrome.append(prod)
                print pdrome
                bol = True
                break
    if bol == True:
        break
        
# Answer: 580085
