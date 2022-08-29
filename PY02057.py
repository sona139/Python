n, m = [int(i) for i in input().split()]
mt = []
mx, mn = -1, 999999
for i in range(n):
    list = [int(i) for i in input().split()]
    mx = max(mx, max(list))
    mn = min(mn, min(list))
    mt += [list]
num = 0
for i in mt:
    for j in i:
        if j == mx-mn:
            num = mx-mn
            break
if num == 0: print('NOT FOUND')
else:
    print(num)
    for i in range(n):
        for j in range(m):
            if int(mt[i][j]) == num:
                print('Vi tri [{}][{}]'.format(i, j))