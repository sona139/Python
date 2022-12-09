parent = [-1]*(100001)

def par(u):
    return u if parent[u] == -1 else par(parent[u])

def union(x, y):
    px = par(x)
    py = par(y)
    if px == py: return
    if px > py: px, py = py, px
    parent[py] = px
    
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if z == 1: union(x, y)
    else: print(int(par(x) == par(y)))