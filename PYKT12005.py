for _ in range(int(input())):
    n, c, d = map(int, input().split())
    l = [int(i) for i in input().split()]
    l.sort()
    c, d = min(c, d), max(c, d)
    s1 = sum(l[-1:-1-c:-1])
    s2 = sum(l[-1-c:-1-c-d:-1])
    print('{:.6f}'.format(s1/c+s2/d))