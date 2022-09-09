for __ in range(int(input())):
    num = input()
    k = input()
    res, left = 0, 0
    index = num.find(k, left)
    while index != -1:
        res += 1
        left = index + len(k)
        index = num.find(k, left)
    print(res)