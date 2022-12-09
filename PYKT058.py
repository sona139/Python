def DFS(u, v, path):
    global g, res
    if u == v:
        path.pop(-1)
        res.append(path)
        return 
    for i in g[u]:
        if not vst[i]:
            vst[i] = 1
            DFS(i, v, path + [i])
            vst[i] = 0

for _ in range(int(input())):
    n, m, u, v = [int(i) for i in input().split()]
    g = [[] for _ in range(n+1)]
    for i in range(m):
        args = input().split()
        g[int(args[0])].append(int(args[1]))
    res = []
    for i in g[u]:
        vst = [0]*(n+1)
        path = [i]
        vst[i] = 1
        DFS(i, v, path)
    
    cnt = [0]*(n+1)
    for path in res:
        for i in path:
            cnt[i] += 1
    ans = 0
    for i in cnt:
        if cnt[i] == len(res) :
            ans += 1
    print(ans)