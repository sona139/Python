n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
sum_up, sum_down = 0, 0
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            sum_up += matrix[i][j]
        elif j >= n-i:
            sum_down += matrix[i][j]
k = int(input())
num = abs(sum_up - sum_down)
print('YES' if num <= k else 'NO')
print(num)
