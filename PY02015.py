while True:
    list = [int(i) for i in input().split()]
    if list.count(0) == 4:
        break
    cnt = 0
    while list.count(list[0]) != 4:
        newlist = list.copy()
        for i in range(4):
            list[i] = abs(newlist[i]-newlist[(i+1)%4])
        cnt += 1
    print(cnt)
        