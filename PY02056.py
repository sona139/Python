n, m = [int(i) for i in input().split()]
mt = []
for i in range(n):
    mt += [input().split()]
num = 0
for i in mt:
    for j in i:
        if len(j) > 1 and j == j[::-1]:
            num = max(num, int(j))
if num == 0: print('NOT FOUND')
else:
    print(num)
    for i in range(n):
        for j in range(m):
            if int(mt[i][j]) == num:
                print('Vi tri [{}][{}]'.format(i, j))