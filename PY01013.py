import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for case in range(int(input())):
    num1, num2 = [int(i) for i in input().split()]
    print('YES' if isprime(sum(int(i) for i in str(math.gcd(num1, num2)))) else 'NO')