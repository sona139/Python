for case in range(int(input())):
    num = int(input())
    l = 1 if num%2 else 2
    sum = 0
    for i in range(l, num+1, 2):
        sum += 1/i
    print('{:.6f}'.format(sum))