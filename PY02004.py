n = int(input())
list = [i for i in input().split()]
cnt = 0
for i in range(1, n):
    if list[i] != list[i-1]:
        cnt += 1
print(cnt)