from math import sqrt
from sys import setrecursionlimit

setrecursionlimit(100000)
CONST = 3+sqrt(5)

def pow(n):
    if n == 0: return 1
    tmp = pow(n//2)
    if n&1: return tmp*tmp*CONST
    return tmp*tmp

for _ in range(int(input())):
    n = int(input())
    print('{0:0>3}'.format(int(pow(n)))[-1:-4:-1][::-1])
    