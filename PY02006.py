def chicken(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

for __ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    print(chicken(a, b, n))