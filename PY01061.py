import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for case in range(int(input())):
    num = '{0:0>3}'.format(input())
    num1, num2 = int(num[:3]), int(num[-1:-4:-1])
    print('YES' if isprime(num1) and isprime(num2) else 'NO')