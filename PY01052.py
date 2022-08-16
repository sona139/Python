import math


def isprime(n):
    if n < 2:
        return 'NO'
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(isprime(sum(map(int, ' '.join(input()).split()))))