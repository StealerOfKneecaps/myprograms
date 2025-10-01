import math
def isPrime(primeCheck):
    for i in range (2, math.floor(primeCheck**0.5)+1):
        if primeCheck%i==0:
            return False
    return True
for i in range (2, 1000000):
    if isPrime(i):
        print (i)