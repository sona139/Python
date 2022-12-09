def solve(n, flag):
    global cnt
    while n > 0:
        mod = n%10
        n //= 10
        for i in range(1, mod+1):
            cnt[i] += flag
        m = n
        while m > 0:
            cnt[m % 10] += (mod+1) * flag
            m //= 10
        for i in range(10):
            cnt[i] += n*flag
        flag *= 10
        n -= 1
        
for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    cnt = [0]*10
    solve(b, 1)
    solve(a-1, -1)
    print(*cnt)