import  math

PRIME = '2357'
UNPRIME = '014689'

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def deff(num):
    if not isprime(len(num)):
        return 'NO'
    return 'YES' if sum(num.count(i) for i in PRIME) > sum(num.count(i) for i in UNPRIME) else 'NO'

for case in range(int(input())):
    print(deff(' '.join(input()).split()))