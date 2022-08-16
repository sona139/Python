import math


def deff(num1, num2):
    return 'YES' if math.gcd(num1, num2) == 1 else 'NO'
for case in range(int(input())):
    num = input()
    print(deff(int(num), int(num[::-1])))