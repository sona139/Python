n = int(input())
list = [int(i) for i in input().split()]
res, num = 1e9, 1e9
for i in list:
    s = sum(abs(i-j) for j in list)
    if res > s:
        res = s
        num = i
print(res, num)