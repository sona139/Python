from math import gcd


n = int(input())
list = sorted([int(i) for i in input().split()])
for i in range(n):
    for j in range(i, n):
        if gcd(list[i], list[j]) == 1:
            print(list[i], list[j])