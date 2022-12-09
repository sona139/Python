n = int(input())
path = [0]*(n+1)

for _ in range(n-1):
    p = [int(i) for i in input().split()]
    path[p[0]] += 1
    path[p[1]] += 1

print('Yes' if path.count(1) == n-1 else 'No')