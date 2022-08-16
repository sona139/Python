def deff(num):
    mul = 1
    for i in num:
        mul *= int(i)
    return mul

for case in range(int(input())):
    n = int(input())
    print(*sorted([i for i in input().split()], key=lambda e: (deff(e), int(e))))