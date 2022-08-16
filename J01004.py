import math

def isprime(n):
    if n < 2:
        return 'NO'
    sqr = int(1+math.sqrt(n))
    for i in range(2, sqr):
        if n%2 == 0:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(isprime(int(input())))