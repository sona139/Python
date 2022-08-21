a, k, n = [int(i) for i in input().split()]
bg = (a//k + 1)*k
if bg > n:
    print(-1)
else:
    for i in range(bg, n+1, k):
        print(i-a, end=' ')
    print()