from math import gcd
from sys import stdin

list = []
for line in stdin:
    for num in line.split():
        list.append(int(num))
        

def solve():
    global n, k, l
    res = n+1
    for i in range(n):
        g = 0
        for j in range(i, n):
            g = l[i] if i == j else gcd(g, l[j])
            if g == k:
                res = min(res, j-i+1)
                break
            if g < k: break
    return res

it = iter(list)
for _ in range(next(it)):
    n, k = next(it), next(it)
    l = [next(it) for __ in range(n)]
    print(solve())