import math

PRIME = '2357'

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def deff(str):
    for i in range(0, len(str)):
        if isprime(i) and str[i] not in PRIME or not isprime(i) and str[i] in PRIME:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(deff(input()))