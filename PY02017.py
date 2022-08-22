for case in range(int(input())):
    n = int(input())
    list = [int(i) for i in input().split()]
    d = dict()
    for i in list:
        try:
            d[i] += 1
        except:
            d[i] = 1
    for i in d:
        if d.get(i)%2:
            print(i)
            break