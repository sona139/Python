move_i = [-1, -1, -1, 0, 0, 1, 1, 1]
move_j = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = [int(i) for i in input().split()] 
mt = [[0]*(m+2)] + [[0] + [int(i) for i in input().split()] + [0] for _ in range(n)] + [[0]*(m+2)]
vis = [[False]*(m+2) for _ in range(n+2)]
 
sum = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if mt[i][j] == -1:
            for k in range(8):
                new_i, new_j = i+move_i[k], j+move_j[k]
                if vis[new_i][new_j] == False:
                    sum += mt[new_i][new_j]
                    vis[new_i][new_j] = True
print(sum)