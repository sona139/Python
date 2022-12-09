from math import log2


for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    res = 0
    for i in range(1, n):
        ma, mi = max(l[i], l[i-1])-1, min(l[i], l[i-1])
        k = int(ma//mi)
        if k: res += int(log2(k))
    print(res)