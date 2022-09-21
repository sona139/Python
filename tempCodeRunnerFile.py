from math import sqrt

def isprime(n):
    if n == 2 or n == 3:
        return True
    if n < 5 or n%2 == 0 or n%3 == 0: return False
    for i in range(5, int(sqrt(n)+1), 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def solve(l, n):
    sl, sr = 0, sum(l)
    for i in range(n):
        sl += l[i]
        sr -= l[i]
        if isprime(sl) and isprime(sr):
            return i
    return 'NOT FOUND'
        
n = int(input())
l = list({int(i):None for i in input().split()})
print(l)
print(solve(l, n))