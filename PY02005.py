n = int(input())
list = [int(i) for i in input().split()]
res = 0
for i in range(n):
    for j in range(i+1, n):
        if i < j and list[i] > list[j]:
            res += 1
print(res)