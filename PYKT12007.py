for _ in range(int(input())):
    n = int(input())
    u = float(input())
    l = [float(i) for i in input().split()]
    l.sort(reverse=True)
    s = sum(l)
    if (u+s)/n >= 1:
        print('1.000000')
        continue
    res, i = 1, 0
    while l[i] > (s+u)/(n-i):
        res *= l[i]
        s -= l[i]
        i += 1
    res *= ((s+u)/(n-i))**(n-i)
    print('1.000000' if res >= 1 else '{:.6f}'.format(res))