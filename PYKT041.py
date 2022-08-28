n = int(input())
l = [' '.join(input()).split() for i in range(n)]
c = []
for i in range(n+1):
    c += [[0]*(n+1)]
for i in range(n+1):
    c[i][0], c[i][i] = 1, 1
for i in range(1, n+1):
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]
res = 0
for i in l:
    res += c[i.count('C')][2]
for i in range(n):
    cnt = 0
    for j in range(n):
        if l[j][i] == 'C':
            cnt += 1
    res += c[cnt][2]
print(res)