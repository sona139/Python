import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def deff(list):
    if not isprime(sum(list)):
        return 'NO'
    for i in range(0, len(list)):
        if (i+list[i])%2:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(deff(list(map(int, ' '.join(input()).split()))))