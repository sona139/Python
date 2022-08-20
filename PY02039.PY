n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
sum_up, sum_down = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            sum_up += matrix[i][j]
        elif i > j:
            sum_down += matrix[i][j]
k = int(input())
num = abs(sum_up - sum_down)
print('YES' if num <= k else 'NO')
print(num)