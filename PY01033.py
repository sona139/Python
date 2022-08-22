from math import gcd


l, r = [int(i) for i in input().split()]
for i in range(l, r):
    for j in range(i+1, r):
        for z in range(j+1, r+1):
            if gcd(i, j) == 1 and gcd(i, z) == 1 and gcd(j, z) == 1:
                print(tuple([i, j, z]))