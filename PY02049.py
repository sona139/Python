for _ in range(int(input())):
    n, p = [int(i) for i in input().split()]
    res = 0
    for i in range(p, n+1, p):
        num = i;
        while num%p == 0:
            num /= p
            res += 1
    print(res)