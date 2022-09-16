n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
p = [[b[i]-a[i], i] for i in range(n)]
p.sort(reverse=True)
# print(p)
print(sum(a[p[x][1]] for x in range(k)) + sum(b[p[x][1]] if b[p[x][1]] < a[p[x][1]] else a[p[x][1]] for x in range(k, n)))