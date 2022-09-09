n, m = [int(i) for i in input().split()]
matrix = []
for i in range(n):
    matrix += [input().split()]
res = 0
for i in matrix:
    for j in i:
       if len(j) > 1 and j == j[::-1]:
           res = max(res, int(j))
if not res:
    print('NOT FOUND')
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == str(res):
                print('Vi tri [{}][{}]'.format(i, j))