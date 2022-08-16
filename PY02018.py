def deff():
    n = int(input())
    list = [0] + [int(i) for i in input().split()] + [n+3]
    for i in range(n+2):
        if list[i] != i:
            return i
    
print(deff())