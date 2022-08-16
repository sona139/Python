for case in range(int(input())):
    input()
    m1, m2, m3 = 1e9, 1e9, 1e9
    for i in input().split():
        num = int(i)
        if m1 > num:
            m1 = num
        elif m2 > num:
            m2 = num
        else:
            m3 = min(m3, num)
    print(m1+m2+m3)