def dfs(u):
    global vst, g
    for v in g[u]:
        if not vst[v]:
            vst[v] = 1
            dfs(v)

for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for __ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    vst = [0]*(n+1)
    cnt = 0
    for u in range(1, n+1):
        if not vst[u]:
            cnt += 1
            dfs(u)
    
    lt_max, res = 0, 0    
    for i in range(1, n+1):
        vst = [0]*(n+1)
        vst[i] = 1
        lt = 0
        for u in range(1, n+1):
            if not vst[u]:
                lt += 1
                dfs(u)
        if lt > lt_max:
            res = i
            lt_max = lt
    
    print(res if lt_max != cnt else 0)
