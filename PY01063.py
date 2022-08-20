for case in range(int(input())):
    str, num = input(), input()
    cnt, index = 0, str.find(num)
    while index != -1:
        cnt += 1
        index = str.find(num, index+len(num))
    print(cnt)