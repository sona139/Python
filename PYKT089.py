n = int(input())
list = []
while True:
    try:
        list += [int(i) for i in input().split()]
    except EOFError:
        break
map = [0]*len(list)
c, l = [], []
for i in range(n):
    if list[i]%2:
        l += [list[i]]
    else:
        map[i] = 1
        c += [list[i]]
c.sort()
l.sort(key=lambda ele: -ele)
i, j = 0, 0
for k in range(n):
    if map[k]:
        print(c[i], end=' ')
        i += 1
    else:
        print(l[j], end=' ')
        j += 1