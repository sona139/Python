n, m = [int(i) for i in input().split()]
list = []
for _ in range(n):
    list.append([int(i) for i in input().split()])

if n > m:
    rows = [0]*n
    for i in range(0, n-m):
        rows[i*2] = 1
    for i in range(n):
        if not rows[i]:
            print(*list[i])

else:
    cols = [0]*m
    for i in range(0, m-n):
        cols[i*2+1] = 1
    for i in range(n):
        for j in range(m):
            if not cols[j]:
                print(list[i][j], end=' ')
        print()