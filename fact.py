#!/usr/bin/env python
import time
from functools import reduce
import asyncio

#More readable, slightly slower since using pre-define function divmod                
def getFactor1(number):
    fact = []
    for i in range(1, int(number**0.5)+1):
        d, m = divmod(number, i)
        if m == 0:
            #if i not in fact:
            fact.append(d)
            if d != int(number/d):
                fact.append(int(number/d))       
    return set(fact)
    
#Slightly simple to execute and more faster, hard to read
def getFactor2(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))   

#Empat Alternatif fungsi H
#1. Total O(n^3/2) --> Mencari faktor satu-satu (linear search dari 1 sampai akhir nomor)
def H1(numberRange, numFactor):
    start = time.time()
    h = []
    reduceNums = []
    for i in range(numberRange, 0, -1):
        getFactor_i = getFactor2(i)
        if len(getFactor_i) == numFactor:
            h.append(i)
    print(time.time()-start)
    return len(h)

#2. Total O(n^2 - sedikit) --> tidak lebih efisien dari algoritma linear search sebelumnya    
def H2(numberRange, numFactor):
    start = time.time()
    h = []
    reduceNums = []

    for i in range(numberRange, numberRange*2//3, -1):
        getFactor_i = getFactor2(i)
        _len        = len(getFactor_i)
        if _len == numFactor:
            reduceNums = reduceNums + list(getFactor_i)
            h.append(i)
            
    for i in list(set(range(numberRange*2//3 - 1, 0, -1)) - set(reduceNums)):
        getFactor_i = getFactor2(i)
        if len(getFactor_i) == numFactor:
            h.append(i)
            
    print(time.time()-start)
    return len(h)

#3. Total O(n^2 - sedikit) --> tidak lebih efisien dari algoritma linear search sebelumnya
def H3(numberRange, numFactor):
    start = time.time()
    h = []
    reduceNums = []

    for i in range(numberRange, numberRange//2, -1):
        getFactor_i = getFactor2(i)
        _len        = len(getFactor_i)
        if _len >= numFactor:
            reduceNums = reduceNums + list(getFactor_i)
            #h.append(i)
            
    for i in set(list(range(numberRange//2 - 1, 0, -1)) + (reduceNums)):
        getFactor_i = getFactor2(i)
        if len(getFactor_i) == numFactor:
            h.append(i)
            
    print(time.time()-start)
    return len(h)

#4. Total O(1/2*n^3/2) --> lebih efisien lebih dari 1/2 x dari algoritma linear search sebelumnya karena mengabaikan faktor ganjil
def H4(numberRange, numFactor=6):
    start = time.time()
    num = 0
    reduceNums = []
    for i in range(numberRange, 0, -1):
        #print(str(getFactor2(i)))
        """if (int(i**0.5)**2) != i: #Ganjil skip
            if len(getFactor2(i)) == numFactor:
                num+=1
        """
        if (int(i**0.5)**2) != i:               #Faktor ganjil skip, karena mencari 6 faktor
            j = 0
            for k in range(1, int(i**0.5)+1):   #Mencari faktor
                if i % k == 0:
                    j += 1
                    if j == 3:                  
                        num += 1
                    if j > 3:                   #Jika tidak ketemu 6 faktor lanjut
                        num -= 1
                        break
    print(time.time()-start)                    
    return num

async def asyncH(startRange, endRange, numFactor=6):
    #start = time.time()
    num = 0
    reduceNums = []
    for i in range(startRange, endRange, -1):
        #print(i)
        #print(str(getFactor2(i)))
        """if (int(i**0.5)**2) != i: #Ganjil skip
            if len(getFactor2(i)) == numFactor:
                num+=1
        """
        if (int(i**0.5)**2) != i:               #Faktor ganjil skip, karena mencari 6 faktor
            j = 0
            for k in range(1, int(i**0.5)+1):   #Mencari faktor
                if i % k == 0:
                    j += 1
                    if j == 3:                  
                        num += 1
                    if j > 3:                   #Jika tidak ketemu 6 faktor lanjut
                        num -= 1
                        break
    #print(time.time()-start)                    
    return num

#4. H4 ditambah fungsi async. Lebih cepat 2/3 x dari sebelumnya tapi memakan resource
async def H5(numberRange, numFactor=6):
    a, b, c, d, e, f, g, h, i, j = await asyncio.gather(asyncH(numberRange, numberRange*9//10,numFactor), asyncH(numberRange*9//10-1, numberRange*8//10,numFactor), asyncH(numberRange*8//10-1, numberRange*7//10,numFactor), asyncH(numberRange*7//10-1, numberRange*6//10,numFactor), asyncH(numberRange*5//10-1, numberRange*4//10,numFactor), asyncH(numberRange*5//10, numberRange*4//10,numFactor), asyncH(numberRange*4//10-1, numberRange*3//10,numFactor), asyncH(numberRange*3//10-1, numberRange*2//10,numFactor), asyncH(numberRange*2//10-1, numberRange//10,numFactor), asyncH(numberRange//10-1, 0,numFactor))
    return a + b + c + d + e + f + g + h + i + j
    
#H(128) = 19, H(1024) = 112, H(16384) = 1168, H(262144) = 13208, H(134217728) = 3969187
#H1 0.0005464553833007812 s
#H4 0.0002923011779785156 s

#H1 0.0058095455169677734 s
#H4 0.0031270980834960938 s

#H1 0.1832265853881836 s
#H4 0.08304572105407715 s

#H1 8.366977214813232 s
#H4 3.344947099685669 s

#H4 25724.061009645462 s

print(H4(262144,6))
print(H4(134217728,6))