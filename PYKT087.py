for _ in range(int(input())):
    n, k = map(int, input().split())
    k = '{0:b}'.format(k)[::-1]
    pow = 1
    res = 0
    for i in range(len(k)):
        res += pow*int(k[i])
        pow *= n
    print(res%1000000007)