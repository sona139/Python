for case in range(int(input())):
    str = input()
    res = ''
    for i in range(0, len(str), 2):
        res += str[i]*int(str[i+1])
    print(res)