import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for case in range(int(input())):
    num = int('{0:0>4}'.format(input()[-1:-5:-1][::-1]))
    print('YES' if isprime(num) else 'NO')