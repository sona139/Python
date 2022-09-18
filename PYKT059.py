from queue import Queue

n, m, k = [int(i) for i in input().split()]
g = []
for _ in range(n+1):
    g += [[]]
for _ in range(m):
    u, v = [int(i) for i in input().split()]
    g[u] += [v]
    g[v] += [u]
q = Queue()
q.put(k)
vst = [0]*(n+1)
vst[k] = 1
while not q.empty():
    u = q.get()
    for v in g[u]:
        if not vst[v]:
            q.put(v)
            vst[v] = 1
res = list(filter(lambda ele: not vst[ele], [i for i in range(1, n+1)]))
print(*res if len(res) else 0, sep='\n')