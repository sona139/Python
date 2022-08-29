from math import sqrt

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)+1)):
        if not n%i:
            return False
    return True

n = int(input())
l = [int(i) for i in input().split()]
lPrime = []
indexPrime = [0]*n
for i in range(n):
    if isPrime(l[i]):
        lPrime += [l[i]]
        indexPrime[i] = 1
lPrime.sort()
j = 0
for i in range(n):
    if indexPrime[i]:
        l[i] = lPrime[j]
        j += 1
print(*l)