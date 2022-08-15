def solve():
    n = int(input())
    list = [int(i) for i in input().split()]
    cnt = 0
    for i in list:
        cnt = list.count(i)
        if cnt > n/2:
            return i
    return 'NO'

for case in range(int(input())):
    print(solve())