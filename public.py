import math
import random

def isPrime(n):
    if n > 1:
        for i in range(2, int((n/2) + 1)):
            if (n % i == 0):
                return False
                break
            else:
                return True
    else:
        return False

#random prime n bits
def nBitsRandomPrime(n):
    while True:
        x = (random.randrange(2**(n-1) + 1, 2**n - 1))
        if (isPrime(x)):
            return x
            break


P = nBitsRandomPrime(160)
ALPHA = 2