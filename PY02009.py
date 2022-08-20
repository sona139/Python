for case in range(int(input())):
    map = [0]*10001
    for i in range(int(input())):
        map[int(input())] += 1
    res = 1000
    for i in range(1000, -1, -1):
        if map[res] <= map[i]:
            res = i
    print(res)