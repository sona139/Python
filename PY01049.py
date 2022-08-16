import math

PRIME = '2357'
UNPRIME = '014689'

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def deff(list):
    if not isprime(len(list)):
        return 'NO'
    return 'YES' if sum(list.count(i) for i in PRIME) > sum(list.count(i) for i in UNPRIME) else 'NO'
    

for case in range(int(input())):
    print(deff(' '.join(input()).split()))